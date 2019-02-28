import re
import unittest

from .api import RubyGems


class TestRubyGems(unittest.TestCase):
    api = RubyGems()

    def test_downloads(self):
        d = self.api.downloads("rake")
        self.assertGreater(d, 0)

    def test_downloads_with_version(self):
        d = self.api.downloads("rake", version="12.2.0")
        self.assertGreater(d, 0)

    def test_downloads_invalid_gem(self):
        s = self.api.downloads("gem_doesnt_exist")
        self.assertIsNone(s)

    def test_downloads_invalid_version(self):
        s = self.api.downloads("rake", version="666.666.666")
        self.assertIsNone(s)

    def test_version(self):
        v = self.api.version("rake")
        match = re.search(r"(\d+\.)*\d+", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_gem(self):
        v = self.api.version("gem_doesnt_exist")
        self.assertIsNone(v)
