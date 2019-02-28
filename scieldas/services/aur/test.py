import re
import unittest

from .api import AUR


class TestArchUserRepository(unittest.TestCase):
    api = AUR()

    def test_version(self):
        v = self.api.version("polybar")
        match = re.search(r"(\d\.)*\d(-\d)*", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_package(self):
        v = self.api.version("package-that-doesnt-exist")
        self.assertIsNone(v)

    def test_license(self):
        license = self.api.license("polybar")
        self.assertEqual(license, "MIT")

    def test_license_invalid_package(self):
        license = self.api.license("package-that-doesnt-exist")
        self.assertIsNone(license)

    def test_votes(self):
        v = self.api.votes("polybar")
        self.assertGreaterEqual(v, 0)

    def test_votes_invalid_package(self):
        v = self.api.votes("package-that-doesnt-exist")
        self.assertIsNone(v)
