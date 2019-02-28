import unittest

from .api import Codecov


class TestCodecov(unittest.TestCase):
    api = Codecov()

    def test_coverage(self):
        coverage = self.api.coverage("github", "codecov", "example-python")
        self.assertGreaterEqual(coverage, 0)
        self.assertLessEqual(coverage, 100)

    def test_coverage_with_branch(self):
        coverage = self.api.coverage(
            "github", "codecov", "example-python", branch="master"
        )
        self.assertGreaterEqual(coverage, 0)
        self.assertLessEqual(coverage, 100)

    def test_coverage_invalid_vcs(self):
        coverage = self.api.coverage("fakevcs", "codecov", "example-python")
        self.assertIsNone(coverage)

    def test_coverage_invalid_user(self):
        coverage = self.api.coverage("github", "fakeuser", "example-python")
        self.assertIsNone(coverage)

    def test_coverage_invalid_repo(self):
        coverage = self.api.coverage("github", "codecov", "fakeproject")
        self.assertIsNone(coverage)

    def test_coverage_invalid_branch(self):
        coverage = self.api.coverage(
            "github", "codecov", "example-python", branch="fakebranch"
        )
        self.assertIsNone(coverage)
