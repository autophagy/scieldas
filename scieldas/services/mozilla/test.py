import re
import unittest

from .api import Mozilla


class TestMozilla(unittest.TestCase):
    api = Mozilla()

    def test_weekly_donwloads(self):
        d = self.api.weekly_downloads("twitter-background-restorer")
        self.assertGreaterEqual(d, 0)

    def test_weekly_downloads_invalid_addon(self):
        d = self.api.weekly_downloads("an-addon-that-doesnt-exist")
        self.assertIsNone(d)

    def test_users(self):
        u = self.api.users("twitter-background-restorer")
        self.assertGreaterEqual(u, 0)

    def test_users_invalid_addon(self):
        u = self.api.users("an-addon-that-doesnt-exist")
        self.assertIsNone(u)

    def test_version(self):
        v = self.api.version("twitter-background-restorer")
        match = re.search(r"(\d\.)*\d", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_addon(self):
        v = self.api.version("an-addon-that-doesnt-exist")
        self.assertIsNone(v)

    def test_rating(self):
        r = self.api.rating("twitter-background-restorer")
        self.assertGreaterEqual(r, 0)
        self.assertLessEqual(r, 5)

    def test_rating_invalid_app(self):
        r = self.api.rating("an-addon-that-doesnt-exist")
        self.assertIsNone(r)
