from typing import Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class Codecov(ServiceAPI):
    base_url = "https://codecov.io/api/"

    @ServiceAPI.call
    def coverage(
        self, vcs: str, user: str, repo: str, api: API, branch: str = None
    ) -> Optional[float]:
        api.add(vcs, user, repo)
        if branch:
            api.add("branches", branch)
        return float(get(api.get(), "commit.totals.c"))
