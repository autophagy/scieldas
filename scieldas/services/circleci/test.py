import unittest

from .api import CircleCI


class TestCodecov(unittest.TestCase):
    api = CircleCI()

    build_statuses = [
        "retried",
        "canceled",
        "infrastructure_fail",
        "timedout",
        "not_run",
        "running",
        "failed",
        "queued",
        "scheduled",
        "not_running",
        "no_tests",
        "fixed",
        "success",
    ]

    def test_build(self):
        build = self.api.build("github", "circleci", "circleci-docs")
        self.assertIn(build, self.build_statuses)

    def test_build_with_branch(self):
        build = self.api.build("github", "circleci", "circleci-docs", branch="master")
        self.assertIn(build, self.build_statuses)

    def test_build_invalid_vcs(self):
        build = self.api.build("fakevcs", "circleci", "circleci-docs")
        self.assertIsNone(build)

    def test_build_invalid_user(self):
        build = self.api.build("github", "fakeuser", "circleci-docs")
        self.assertIsNone(build)

    def test_build_invalid_repo(self):
        build = self.api.build("github", "circleci", "fakeproject")
        self.assertIsNone(build)

    def test_build_invalid_branch(self):
        build = self.api.build(
            "github", "circleci", "circleci-docs", branch="fakebranch"
        )
        self.assertIsNone(build)
