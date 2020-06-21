import unittest

from .api import ReadTheDocs


class TestReadTheDocs(unittest.TestCase):
    api = ReadTheDocs()

    def test_build_status(self):
        s = self.api.build_status("datarum")
        self.assertIn(s, ["pass", "fail"])

    def test_build_status_with_version(self):
        s = self.api.build_status("crate", version="3.3")
        self.assertIn(s, ["pass", "fail"])

    def test_downloads_invalid_project(self):
        s = self.api.build_status("project_doesnt_exist_232323")
        self.assertTrue(s is None)

    def test_downloads_invalid_version(self):
        s = self.api.build_status("crate", version="420.69")
        self.assertTrue(s is None)
