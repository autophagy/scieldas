import unittest
from os import environ

from .api import Travis


class TestTravis(unittest.TestCase):
    api_key = environ.get("TRAVIS_API_KEY")
    api = Travis()

    def test_build_status(self):
        s = self.api.build_status("autophagy", "datarum", self.api_key)
        self.assertIn(s, ["pass", "fail", "building"])

    def test_build_status_with_branch(self):
        s = self.api.build_status("crate", "crate", self.api_key, branch="3.2")
        self.assertIn(s, ["pass", "fail", "building"])

    def test_build_status_invalid_project(self):
        s = self.api.build_status(
            "autophagy", "project_doesnt_exist_232323", self.api_key
        )
        self.assertTrue(s is None)

    def test_build_status_invalid_user(self):
        s = self.api.build_status(
            "user_doesnt_exist", "project_doesnt_exist_232323", self.api_key
        )
        self.assertTrue(s is None)

    def test_build_status_invalid_branch(self):
        s = self.api.build_status("crate", "crate", self.api_key, branch="0.1")
        self.assertTrue(s is None)
