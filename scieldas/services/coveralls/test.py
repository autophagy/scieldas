import unittest

from .api import Coveralls


class TestCoveralls(unittest.TestCase):
    api = Coveralls()

    def test_coverage(self):
        c = self.api.coverage("github", "ambv", "black")
        self.assertTrue(type(c) is float)
        self.assertGreaterEqual(c, 0)
        self.assertLess(c, 100)

    def test_coverage_with_branch(self):
        c = self.api.coverage("github", "crate", "crate", branch="0.54")
        self.assertTrue(type(c) is float)
        self.assertGreaterEqual(c, 0)
        self.assertLess(c, 100)

    def test_coverage_invalid_vcs(self):
        c = self.api.coverage("fakevcs", "ambv", "black")
        self.assertIsNone(c)

    def test_coverage_invalid_user(self):
        c = self.api.coverage("github", "ambv_but_fake", "black")
        self.assertIsNone(c)

    def test_coverage_invalid_project(self):
        c = self.api.coverage("github", "ambv", "white")
        self.assertIsNone(c)
