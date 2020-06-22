import re
import unittest
from os import environ

from .api import Github, GithubWorkflows


class TestGithub(unittest.TestCase):
    token = environ.get("GITHUB_API_KEY")
    api = Github()
    workflowApi = GithubWorkflows()

    def test_watchers(self):
        w = self.api.watchers("crate", "crate", self.token)
        self.assertGreater(w, 0)

    def test_watchers_invalid_owner(self):
        w = self.api.watchers("crate_but_not_real", "crate", self.token)
        self.assertIsNone(w)

    def test_watchers_invalid_repo(self):
        w = self.api.watchers("crate", "an_unreal_project", self.token)
        self.assertIsNone(w)

    def test_forks(self):
        f = self.api.forks("crate", "crate", self.token)
        self.assertGreater(f, 0)

    def test_forks_invalid_owner(self):
        f = self.api.forks("crate_but_not_real", "crate", self.token)
        self.assertIsNone(f)

    def test_forks_invalid_repo(self):
        f = self.api.forks("crate", "an_unreal_project", self.token)
        self.assertIsNone(f)

    def test_license(self):
        license = self.api.license("crate", "crate", self.token)
        self.assertIsInstance(license, str)
        self.assertGreater(len(license), 0)

    def test_license_invalid_owner(self):
        license = self.api.license("crate_but_not_real", "crate", self.token)
        self.assertIsNone(license)

    def test_license_invalid_repo(self):
        license = self.api.license("crate", "an_unreal_project", self.token)
        self.assertIsNone(license)

    def test_stars(self):
        s = self.api.stars("crate", "crate", self.token)
        self.assertGreater(s, 0)

    def test_stars_invalid_owner(self):
        s = self.api.stars("crate_but_not_real", "crate", self.token)
        self.assertIsNone(s)

    def test_stars_invalid_repo(self):
        s = self.api.stars("crate", "an_unreal_project", self.token)
        self.assertIsNone(s)

    def test_top_language(self):
        license = self.api.top_language("crate", "crate", self.token)
        self.assertIsInstance(license, dict)
        self.assertIsInstance(license.get("lang"), str)
        self.assertGreaterEqual(license.get("percentage"), 0)
        self.assertLess(license.get("percentage"), 100)

    def test_top_language_invalid_owner(self):
        w = self.api.top_language("crate_but_not_real", "crate", self.token)
        self.assertIsNone(w)

    def test_top_language_invalid_repo(self):
        license = self.api.top_language("crate", "an_unreal_project", self.token)
        self.assertIsNone(license)

    def test_followers(self):
        f = self.api.followers("autophagy", self.token)
        self.assertGreater(f, 0)

    def test_followers_invalid_username(self):
        f = self.api.followers("a_user_that_doesnt_exist", self.token)
        self.assertIsNone(f)

    def test_latest_release(self):
        r = self.api.latest_release("autophagy", "datarum", self.token)
        match = re.search(r"(\d\.)*\d", r)
        self.assertTrue(match)
        self.assertEqual(match.group(0), r)

    def test_latest_release_invalid_owner(self):
        r = self.api.latest_release("crate_but_not_real", "crate", self.token)
        self.assertIsNone(r)

    def test_latest_release_invalid_repo(self):
        r = self.api.latest_release("crate", "an_unreal_project", self.token)
        self.assertIsNone(r)

    def test_language_count(self):
        c = self.api.language_count("autophagy", "hraew", self.token)
        self.assertGreater(c, 0)

    def test_language_count_invalid_owner(self):
        c = self.api.language_count("a_user_that_doesnt_exist", "hraew", self.token)
        self.assertIsNone(c)

    def test_language_count_invalid_repo(self):
        c = self.api.language_count("autophagy", "an_unreal_project", self.token)
        self.assertIsNone(c)

    def test_downloads(self):
        d = self.api.downloads("twbs", "bootstrap", self.token)
        self.assertGreater(d, 0)

    def test_downloads_with_tag(self):
        d = self.api.downloads("twbs", "bootstrap", self.token, tag="v4.3.1")
        self.assertGreater(d, 0)

    def test_downloads_with_asset(self):
        d = self.api.downloads(
            "twbs",
            "bootstrap",
            self.token,
            tag="v4.3.1",
            asset="bootstrap-4.3.1-dist.zip",
        )
        self.assertGreater(d, 0)

    def test_downloads_invalid_owner(self):
        d = self.api.downloads("user_doesnt_exist", "bootstrap", self.token)
        self.assertIsNone(d)

    def test_downloads_invalid_repo(self):
        d = self.api.downloads("twbs", "bootstrappier", self.token)
        self.assertIsNone(d)

    def test_downloads_invalid_tag(self):
        d = self.api.downloads("twbs", "bootstrap", self.token, tag="v666.666.666")
        self.assertIsNone(d)

    def test_downloads_invalid_asset(self):
        d = self.api.downloads(
            "twbs", "bootstrap", self.token, tag="v4.3.1", asset="fake_file.tar.gz"
        )
        self.assertIsNone(d)

    def test_issues(self):
        i = self.api.issues("crate", "crate", "all", self.token)
        o = self.api.issues("crate", "crate", "open", self.token)
        self.assertGreater(i, 0)
        self.assertGreaterEqual(o, 0)
        self.assertGreater(i, o)

    def test_issues_invalid_owner(self):
        i = self.api.issues("user_doesnt_exist", "crate", "closed", self.token)
        self.assertIsNone(i)

    def test_issues_invalid_repo(self):
        i = self.api.issues("crate", "fake_repo", "open", self.token)
        self.assertIsNone(i)

    def test_issues_invalid_state(self):
        i = self.api.issues("crate", "crate", "half-open", self.token)
        self.assertEqual(i, 0)

    def test_pull_requests(self):
        p = self.api.pull_requests("crate", "crate", "all", self.token)
        o = self.api.pull_requests("crate", "crate", "open", self.token)
        self.assertGreater(p, 0)
        self.assertGreaterEqual(o, 0)
        self.assertGreater(p, o)

    def test_pull_requests_invalid_owner(self):
        p = self.api.pull_requests("user_doesnt_exist", "crate", "closed", self.token)
        self.assertIsNone(p)

    def test_pull_requests_invalid_repo(self):
        p = self.api.pull_requests("crate", "fake_repo", "open", self.token)
        self.assertIsNone(p)

    def test_pull_requests_invalid_state(self):
        p = self.api.pull_requests("crate", "crate", "half-open", self.token)
        self.assertEqual(p, 0)

    def test_workflow_status(self):
        s = self.workflowApi.workflow_status(
            "autophagy", "hlaf", "Continuous Integration", self.token
        )
        self.assertIn(s, ["passing", "failing"])

    def test_workflow_status_invalid_owner(self):
        s = self.workflowApi.workflow_status(
            "user_doesnt_exist", "hlaf", "Continuous Integration", self.token
        )
        self.assertIsNone(s)

    def test_workflow_status_invalid_repo(self):
        s = self.workflowApi.workflow_status(
            "autophagy", "fake_repo", "Continuous Integration", self.token
        )
        self.assertIsNone(s)

    def test_workflow_status_invalid_workflow(self):
        s = self.workflowApi.workflow_status(
            "autophagy", "hlaf", "Continuous Disintegration", self.token
        )
        self.assertIsNone(s)
