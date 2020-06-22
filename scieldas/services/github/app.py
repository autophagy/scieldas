import random
import time

from flask import current_app
from scieldas.models.github_oauth_tokens import refresh_github_oauth
from scieldas.services import Service
from scieldas.shields import StateShield, TextShield

from .api import Github, GithubWorkflows

api = Github()
workflowApi = GithubWorkflows()
time_since_refresh = time.time()


def token():
    if time.time() - time_since_refresh > current_app.config.get(
        "TOKEN_DB_REFRESH_SECONDS"
    ):
        refresh_github_oauth()
    tokens = current_app.config.get("GITHUB_OAUTH_TOKENS")
    return random.choice(tokens)


class Watchers(Service):
    name = "Repository Watchers"
    example = 165
    shield = TextShield(prefix="Watchers")
    base = "github"
    routes = ["watchers/:owner/:repo"]

    def route(self, owner, repo):
        return api.watchers(owner, repo, token())


class Forks(Service):
    name = "Repository Forks"
    example = 332
    shield = TextShield(prefix="Forks")
    base = "github"
    routes = ["forks/:owner/:repo"]

    def route(self, owner, repo):
        return api.forks(owner, repo, token())


class License(Service):
    name = "Repository License"
    example = "Apache License 2.0"
    shield = TextShield(prefix="License")
    base = "github"
    routes = ["license/:owner/:repo"]

    def route(self, owner, repo):
        return api.license(owner, repo, token())


class Stars(Service):
    name = "Repository Stars"
    example = 165
    shield = TextShield(prefix="Stars")
    base = "github"
    routes = ["stars/:owner/:repo"]

    def route(self, owner, repo):
        return api.stars(owner, repo, token())


class TopLanguage(Service):
    name = "Repository Top Language"
    example = "Python (30.2)"
    shield = TextShield(prefix="Language")
    base = "github"
    routes = ["languages/top/:owner/:repo"]

    def route(self, owner, repo):
        top_language = api.top_language(owner, repo, token())
        return f"{top_language.get('lang')} ({top_language.get('percentage')})"


class Followers(Service):
    name = "User Followers"
    example = 92
    shield = TextShield(prefix="Followers")
    base = "github"
    routes = ["followers/:username"]

    def route(self, username):
        return api.followers(username, token())


class LatestRelease(Service):
    name = "Latest Release"
    example = "1.1.2"
    shield = TextShield(prefix="Release")
    base = "github"
    routes = ["release/:owner/:repository"]

    def route(self, owner, repository):
        return api.latest_release(owner, repository, token())


class LanguageCount(Service):
    name = "Repository Language Count"
    example = 4
    shield = TextShield(prefix="Languages")
    base = "github"
    routes = ["languages/count/:owner/:repo"]

    def route(self, owner, repo):
        return api.language_count(owner, repo, token())


class Downloads(Service):
    name = "Asset Downloads"
    example = 120_000
    shield = TextShield(prefix="Downloads")
    base = "github"
    routes = [
        "downloads/:owner/:repo",
        "downloads/:owner/:repo/:tag",
        "downloads/:owner/:repo/:tag/:asset",
    ]

    def route(self, owner, repo, tag=None, asset=None):
        suffix = None
        if asset:
            suffix = f" [{asset}]"
        elif tag:
            suffix = f" {tag}"
        return self.Response(
            api.downloads(owner, repo, token(), tag=tag, asset=asset),
            {"suffix": suffix},
        )


class Issues(Service):
    name = "Github Issues"
    example = 78
    shield = TextShield(prefix="Issues")
    base = "github"
    routes = ["issues/:state(open|closed|all)/:owner/:repo"]

    def route(self, state, owner, repo):
        prefix = None
        if state == "open":
            prefix = "Open Issues"
        elif state == "closed":
            prefix = "Closed Issues"
        return self.Response(
            api.issues(owner, repo, state, token()), {"prefix": prefix}
        )


class PullRequests(Service):
    name = "Github Pull Requests"
    example = 78
    shield = TextShield(prefix="Pull Requests")
    base = "github"
    routes = ["prs/:state(open|closed|all)/:owner/:repo"]

    def route(self, state, owner, repo):
        prefix = None
        if state == "open":
            prefix = "Open Pull Requests"
        elif state == "closed":
            prefix = "Closed Pull Requests"
        return self.Response(
            api.pull_requests(owner, repo, state, token()), {"prefix": prefix}
        )


class WorkflowStatus(Service):
    name = "Github Workflow Status"
    example = "Passing"
    shield = StateShield(
        {"passing": "Passing", "failing": "failing"}, prefix="Workflow"
    )
    base = "github"
    routes = ["workflow/status/:owner/:repo/:workflow"]

    def route(self, owner, repo, workflow):
        status = workflowApi.workflow_status(owner, repo, workflow, token())
        return self.Response(status, {"prefix": workflow})
