from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class Coveralls(ServiceAPI):
    base_url = "https://coveralls.io/"

    @ServiceAPI.call
    def coverage(
        self, vcs: str, user: str, project: str, api: API, branch=None
    ) -> Optional[float]:
        branch = "master" if branch is None else branch
        coveralls_json = api.add(vcs, user, project).get(params={"branch": branch})
        return coveralls_json.get("covered_percent")
