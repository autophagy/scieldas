from collections import namedtuple
from typing import Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI

TestResults = namedtuple("testResults", "passed failed skipped")


class Appveyor(ServiceAPI):
    base_url = "https://ci.appveyor.com/api/projects/"

    @ServiceAPI.call
    def build(
        self, user: str, repo: str, api: API, branch: str = None
    ) -> Optional[str]:
        api.add(user, repo)
        if branch:
            api.add("branch", branch)
        details = api.get()
        return get(details, "build.status")

    @ServiceAPI.call
    def tests(
        self, user: str, repo: str, api: API, branch: str = None
    ) -> Optional[TestResults]:
        total, passed, failed = 0, 0, 0
        api.add(user, repo)
        if branch:
            api.add("branch", branch)
        jobs = get(api.get(), "build.jobs")
        for job in jobs:
            total += job.get("testsCount")
            passed += job.get("passedTestsCount")
            failed += job.get("failedTestsCount")
        return TestResults(
            passed=passed, failed=failed, skipped=total - passed - failed
        )
