import unittest

from .api import DockerHub


class TestDockerhub(unittest.TestCase):
    api = DockerHub()

    def test_build_status(self):
        s = self.api.build_status("autophagy", "forebodere")
        self.assertIn(s, ["pass", "fail", "building"])

    def test_build_status_invalid_project(self):
        s = self.api.build_status("autophagy", "project_doesnt_exist_232323")
        self.assertIsNone(s)

    def test_build_status_invalid_user(self):
        s = self.api.build_status("user_doesnt_exist", "project_doesnt_exist_232323")
        self.assertIsNone(s)

    def test_pulls(self):
        p = self.api.pulls("crate", "crate")
        self.assertGreater(p, 0)

    def test_pulls_invalid_project(self):
        p = self.api.pulls("crate", "fake-project")
        self.assertIsNone(p)

    def test_pulls_invalid_user(self):
        p = self.api.pulls("user_doesnt_exist", "fake-project")
        self.assertIsNone(p)

    def test_stars(self):
        s = self.api.stars("crate", "crate")
        self.assertGreater(s, 0)

    def test_stars_invalid_project(self):
        s = self.api.stars("crate", "fake-project")
        self.assertIsNone(s)

    def test_stars_invalid_user(self):
        s = self.api.stars("user_doesnt_exist", "fake-project")
        self.assertIsNone(s)
