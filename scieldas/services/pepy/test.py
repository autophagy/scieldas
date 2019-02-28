import re
import unittest

from .api import PePy


class TestPePy(unittest.TestCase):
    api = PePy()

    def test_downloads(self):
        d = self.api.downloads("datarum")
        match = re.search(r"([\d.]+[\w]*)+", d)
        self.assertTrue(match)
        self.assertEqual(match.group(0), d)

    def test_downloads_invalid_project(self):
        s = self.api.downloads("project_doesnt_exist_232323")
        self.assertTrue(s is None)
