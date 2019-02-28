import unittest

from .api import Appveyor


class TestAppveyor(unittest.TestCase):
    api = Appveyor()

    build_statuses = ["success", "error"]

    def test_build(self):
        build = self.api.build("gruntjs", "grunt")
        self.assertIn(build, self.build_statuses)

    def test_build_with_branch(self):
        build = self.api.build("gruntjs", "grunt", branch="master")
        self.assertIn(build, self.build_statuses)

    def test_build_invalid_user(self):
        build = self.api.build("fakeuser", "grunt")
        self.assertIsNone(build)

    def test_build_invalid_repo(self):
        build = self.api.build("gruntjs", "fakeproject")
        self.assertIsNone(build)

    def test_build_invalid_branch(self):
        build = self.api.build("gruntjs", "grunt", branch="fakebranch")
        self.assertIsNone(build)

    def test_tests(self):
        tests = self.api.tests("NZSmartie", "coap-net-iu0to")
        self.assertGreaterEqual(tests.passed, 0)
        self.assertGreaterEqual(tests.failed, 0)
        self.assertGreaterEqual(tests.skipped, 0)

    def test_tests_with_branch(self):
        tests = self.api.tests("NZSmartie", "coap-net-iu0to", branch="master")
        self.assertGreaterEqual(tests.passed, 0)
        self.assertGreaterEqual(tests.failed, 0)
        self.assertGreaterEqual(tests.skipped, 0)

    def test_tests_invalid_user(self):
        tests = self.api.tests("fakeuser", "grunt")
        self.assertIsNone(tests)

    def test_tests_invalid_repo(self):
        tests = self.api.tests("gruntjs", "fakeproject")
        self.assertIsNone(tests)

    def test_tests_invalid_branch(self):
        tests = self.api.tests("gruntjs", "grunt", branch="fakebranch")
        self.assertIsNone(tests)
