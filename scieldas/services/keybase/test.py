import unittest

from .api import Keybase


class TestKeybase(unittest.TestCase):
    api = Keybase()

    def test_pgp(self):
        p = self.api.pgp("autophagy")
        self.assertEqual(p, "d7de7c519e26926c5d895cb248a4e913f7236fba")

    def test_pgp_invalid_user(self):
        p = self.api.pgp("a_very_fake_user")
        self.assertIsNone(p)
