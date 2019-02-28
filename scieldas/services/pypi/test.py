import re
import unittest

from .api import PyPi, PyPiStats


class TestPyPi(unittest.TestCase):
    api = PyPi()

    def test_version(self):
        v = self.api.version("datarum")
        match = re.search(r"(\d\.)*\d", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_project(self):
        s = self.api.version("project_doesnt_exist_232323")
        self.assertTrue(s is None)

    def test_pyversions(self):
        pyv = self.api.pyversions("black")
        match = re.search(r"([\d.]+[, ]*)+", pyv)
        self.assertTrue(match)
        self.assertEqual(match.group(0), pyv)

    def test_pyversions_invalid_project(self):
        pyv = self.api.pyversions("project_doesnt_exist_232323")
        self.assertTrue(pyv is None)

    def test_status(self):
        s = self.api.status("black")
        self.assertIn(
            s,
            [
                "Planning",
                "Pre-Alpha",
                "Alpha",
                "Beta",
                "Production/Stable",
                "Mature",
                "Inactive",
            ],
        )

    def test_status_invalid_project(self):
        s = self.api.status("project_doesnt_exist_232323")
        self.assertTrue(s is None)

    def test_format(self):
        f = self.api.format("black")
        self.assertIn(f, ["wheel", "egg", "source"])

    def test_format_invalid_project(self):
        f = self.api.format("project_doesnt_exist_232323")
        self.assertTrue(f is None)

    def test_license(self):
        license = self.api.license("black")
        self.assertEqual(license, "MIT License")

    def test_license_invalid_project(self):
        license = self.api.license("project_doesnt_exist")
        self.assertIsNone(license)


class TestPyPiStats(unittest.TestCase):
    api = PyPiStats()

    def test_downloads_day(self):
        d = self.api.downloads("day", "black")
        self.assertGreaterEqual(d, 0)

    def test_downloads_week(self):
        d = self.api.downloads("day", "black")
        self.assertGreaterEqual(d, 0)

    def test_downloads_month(self):
        d = self.api.downloads("day", "black")
        self.assertGreaterEqual(d, 0)

    def test_downloads_invalid_time_period(self):
        d = self.api.downloads("century", "black")
        self.assertIsNone(d)

    def test_downloads_invalid_project(self):
        d = self.api.downloads("day", "project_doesnt_exist")
        self.assertIsNone(d)
