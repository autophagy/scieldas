import re
import unittest

from .api import Crates


class TestCrates(unittest.TestCase):
    api = Crates()

    def test_downloads(self):
        d = self.api.downloads("libc")
        self.assertGreater(d, 0)

    def test_downloads_with_version(self):
        d = self.api.downloads("libc", version="0.2.50")
        self.assertGreater(d, 0)

    def test_downloads_invalid_crate(self):
        s = self.api.downloads("crate_doesnt_exist")
        self.assertIsNone(s)

    def test_downloads_invalid_version(self):
        s = self.api.downloads("libc", version="666.666.666")
        self.assertIsNone(s)

    def test_version(self):
        v = self.api.version("libc")
        match = re.search(r"(\d+\.)*\d+", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_crate(self):
        v = self.api.version("crate_doesnt_exist")
        self.assertIsNone(v)
