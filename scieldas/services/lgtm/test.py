import unittest

from .api import LGTM


class TestKeybase(unittest.TestCase):
    api = LGTM()

    def test_alerts(self):
        a = self.api.alerts("crate", "crate")
        self.assertGreater(a, 0)

    def test_alerts_invalid_owner(self):
        a = self.api.alerts("a_very_fake_user", "crate")
        self.assertIsNone(a)

    def test_alerts_invalid_repo(self):
        a = self.api.alerts("crate", "fake_repo")
        self.assertIsNone(a)

    def test_grade(self):
        g = self.api.grade("java", "crate", "crate")
        self.assertIn(g, ["A+", "A", "B", "C", "D", "E"])

    def test_grade_invalid_lang(self):
        g = self.api.grade("brainfuck", "crate", "crate")
        self.assertIsNone(g)

    def test_grade_invalid_owner(self):
        g = self.api.grade("java", "a_very_fake_user", "crate")
        self.assertIsNone(g)

    def test_grade_invalid_repo(self):
        g = self.api.grade("java", "crate", "fake_repo")
        self.assertIsNone(g)
