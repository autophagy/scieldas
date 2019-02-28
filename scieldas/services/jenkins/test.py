import unittest

from .api import Jenkins


class TestCoveralls(unittest.TestCase):
    api = Jenkins()

    def test_installs(self):
        i = self.api.installs("jquery")
        self.assertGreater(i, 0)

    def test_installs_with_version(self):
        total = self.api.installs("jquery")
        i = self.api.installs("jquery", version="1.12.4-0")
        self.assertGreater(i, 0)
        self.assertGreater(total, i)

    def test_installs_invalid_plugin(self):
        i = self.api.installs("fake_plugin")
        self.assertIsNone(i)

    def test_installs_with_invalid_version(self):
        i = self.api.installs("jquery", version="fakeversion")
        self.assertIsNone(i)
