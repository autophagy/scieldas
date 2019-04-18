from typing import Dict, Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class Github(ServiceAPI):
    base_url = "https://api.github.com/"

    @ServiceAPI.call
    def watchers(self, owner: str, repo: str, token: str, api: API) -> Optional[int]:
        repo_info = api.add("repos", owner, repo).get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return repo_info.get("subscribers_count")

    @ServiceAPI.call
    def forks(self, owner: str, repo: str, token: str, api: API) -> Optional[int]:
        repo_info = api.add("repos", owner, repo).get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return repo_info.get("forks_count")

    @ServiceAPI.call
    def license(self, owner: str, repo: str, token: str, api: API) -> Optional[str]:
        repo_info = api.add("repos", owner, repo).get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return get(repo_info, "license.name")

    @ServiceAPI.call
    def stars(self, owner: str, repo: str, token: str, api: API) -> Optional[int]:
        repo_info = api.add("repos", owner, repo).get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return repo_info.get("stargazers_count")

    @ServiceAPI.call
    def top_language(
        self, owner: str, repo: str, token: str, api: API
    ) -> Optional[Dict]:
        languages = api.add("repos", owner, repo, "languages").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        top_lang = None
        top_size, total = 0, 0
        for lang, size in languages.items():
            if size > top_size:
                top_lang = lang
                top_size = size
            total += size
        if top_lang is None:
            return None
        else:
            return {"lang": top_lang, "percentage": round((top_size / total) * 100, 1)}

    @ServiceAPI.call
    def followers(self, username: str, token: str, api: API) -> Optional[int]:
        user_info = api.add("users", username).get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return user_info.get("followers")

    @ServiceAPI.call
    def latest_release(
        self, owner: str, repo: str, token: str, api: API
    ) -> Optional[str]:
        release_info = api.add("repos", owner, repo, "releases", "latest").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return release_info.get("tag_name")

    @ServiceAPI.call
    def language_count(
        self, owner: str, repo: str, token: str, api: API
    ) -> Optional[int]:
        languages = api.add("repos", owner, repo, "languages").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return len(languages)

    @ServiceAPI.call
    def downloads(
        self, owner: str, repo: str, token: str, api: API, tag=None, asset=None
    ):
        releases = api.add("repos", owner, repo, "releases").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        download_count = 0
        for release in releases:
            if tag and release.get("tag_name") == tag:
                for a in release.get("assets"):
                    if asset and a.get("name") == asset:
                        return a.get("download_count")
                    elif not asset:
                        download_count += a.get("download_count")
                if asset:
                    return None
                return download_count
            elif not tag:
                for asset in release.get("assets"):
                    download_count += asset.get("download_count")
        if tag:
            return None
        return download_count

    @ServiceAPI.call
    def issues(self, owner: str, repo: str, state: str, token: str, api: API):
        state_map = {"open": "+is:open", "closed": "+is:closed", "all": ""}
        query = f"?q=repo:{owner}/{repo}+is:issue{state_map.get(state, state)}"
        api.suffix = query
        issues = api.add("search", "issues").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return issues.get("total_count")

    @ServiceAPI.call
    def pull_requests(self, owner: str, repo: str, state: str, token: str, api: API):
        state_map = {"open": "+is:open", "closed": "+is:closed", "all": ""}
        query = f"?q=repo:{owner}/{repo}+is:pr{state_map.get(state, state)}"
        api.suffix = query
        issues = api.add("search", "issues").get(
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}",
            }
        )
        return issues.get("total_count")
