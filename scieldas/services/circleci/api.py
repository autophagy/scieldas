from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class CircleCI(ServiceAPI):
    base_url = "https://circleci.com/api/v1.1/project/"

    @ServiceAPI.call
    def build(
        self, vcs: str, user: str, repo: str, api: API, branch: str = None
    ) -> Optional[str]:
        api.add(vcs, user, repo)
        if branch:
            api.add("tree", branch)
        details = api.get(params={"filter": "completed", "limit": 1})
        if len(details) == 0:
            return None
        return details[0].get("status")
