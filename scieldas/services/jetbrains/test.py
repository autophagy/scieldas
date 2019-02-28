import re
import unittest

from .api import Jetbrains


class TestJetbrains(unittest.TestCase):
    api = Jetbrains()

    def test_downloads(self):
        downloads = self.api.downloads("1347-scala")
        self.assertGreaterEqual(downloads, 0)

    def test_downloads_invalid_id(self):
        downloads = self.api.downloads("666-fakeplugin")
        self.assertIsNone(downloads)

    def test_version(self):
        version = self.api.version("1347-scala")
        match = re.search(r"(\d*\.)*\d+", version)
        self.assertTrue(match)
        self.assertEqual(match.group(0), version)

    def test_version_invalid_id(self):
        version = self.api.version("666-fakeplugin")
        self.assertIsNone(version)
