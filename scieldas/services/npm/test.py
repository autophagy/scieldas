import re
import unittest

from .api import NPM, NPMRegistry


class TestNPMRegistry(unittest.TestCase):
    api = NPMRegistry()

    def test_license(self):
        license = self.api.license("request")
        self.assertIsInstance(license, str)
        self.assertGreater(len(license), 0)

    def test_license_invalid_package(self):
        license = self.api.license("invalid_package")
        self.assertIsNone(license)

    def test_version(self):
        v = self.api.version("request")
        match = re.search(r"(\d\.)*\d*(\.\d)*", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_package(self):
        v = self.api.version("invalid_package")
        self.assertIsNone(v)


class TestNPM(unittest.TestCase):
    api = NPM()

    def test_downloads(self):
        t = self.api.downloads("total", "request")
        y = self.api.downloads("year", "request")
        m = self.api.downloads("month", "request")
        w = self.api.downloads("week", "request")
        self.assertGreater(t, 0)
        self.assertGreater(y, 0)
        self.assertGreater(m, 0)
        self.assertGreater(w, 0)
        self.assertLess(y, t)
        self.assertLess(m, y)
        self.assertLess(w, m)

    def test_downloads_invalid_package(self):
        t = self.api.downloads("total", "invalid_package")
        self.assertIsNone(t)

    def test_downloads_invalid_period(self):
        t = self.api.downloads("century", "request")
        self.assertIsNone(t)
