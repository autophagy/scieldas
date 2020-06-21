import re
import unittest

from .api import Chrome


class TestChromeWebStore(unittest.TestCase):
    api = Chrome()

    def test_version(self):
        v = self.api.version(
            "gcjejnlljikllkloanankijokfbaelhi"
        )  # Twitter Background Restorer
        match = re.search(r"(\d\.)*\d", v)
        self.assertTrue(match)
        self.assertEqual(match.group(0), v)

    def test_version_invalid_app(self):
        v = self.api.version("an-app-that-doesnt-exist")
        self.assertIsNone(v)

    def test_users(self):
        u = self.api.users(
            "gcjejnlljikllkloanankijokfbaelhi"
        )  # Twitter Background Restorer
        match = re.search(r"^(\d)+(,)+(\d)*(\+)*$", u)
        self.assertTrue(match)
        self.assertEqual(match.group(0), u)

    def test_users_invalid_app(self):
        u = self.api.users("an-app-that-doesnt-exist")
        self.assertIsNone(u)

    def test_rating(self):
        r = self.api.rating(
            "gcjejnlljikllkloanankijokfbaelhi"
        )  # Twitter Background Restorer
        self.assertGreaterEqual(r, 0)
        self.assertLessEqual(r, 5)

    def test_rating_invalid_app(self):
        r = self.api.rating("an-app-that-doesnt-exist")
        self.assertIsNone(r)
