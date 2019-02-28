import unittest

from .api import Mastodon


class TestMastodon(unittest.TestCase):
    api = Mastodon()

    def test_users(self):
        u = self.api.users("mastodon.social")
        self.assertGreater(u, 0)

    def test_users_invalid_instance(self):
        u = self.api.users("afakemastodon.social")
        self.assertIsNone(u)

    def test_statuses(self):
        s = self.api.statuses("mastodon.social")
        self.assertGreater(s, 0)

    def test_statuses_invalid_instance(self):
        s = self.api.statuses("afakemastodon.social")
        self.assertIsNone(s)

    def test_domains(self):
        d = self.api.domains("mastodon.social")
        self.assertGreater(d, 0)

    def test_domains_invalid_instance(self):
        d = self.api.domains("afakemastodon.social")
        self.assertIsNone(d)
