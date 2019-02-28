import unittest

from .api import Discourse


class TestDiscourse(unittest.TestCase):
    api = Discourse()

    def test_users(self):
        users = self.api.users("meta.discourse.org")
        self.assertGreater(users, 0)

    def test_users_invalid_instance(self):
        users = self.api.users("feta.discourse.org")
        self.assertIsNone(users)

    def test_posts(self):
        posts = self.api.posts("meta.discourse.org")
        self.assertGreater(posts, 0)

    def test_posts_invalid_instance(self):
        posts = self.api.posts("feta.discourse.org")
        self.assertIsNone(posts)

    def test_topics(self):
        topics = self.api.topics("meta.discourse.org")
        self.assertGreater(topics, 0)

    def test_topics_invalid_instance(self):
        topics = self.api.topics("feta.discourse.org")
        self.assertIsNone(topics)

    def test_likes(self):
        likes = self.api.likes("meta.discourse.org")
        self.assertGreater(likes, 0)

    def test_likes_invalid_instance(self):
        likes = self.api.likes("feta.discourse.org")
        self.assertIsNone(likes)

    def test_status(self):
        status = self.api.status("meta.discourse.org")
        self.assertTrue(status)

    def test_status_invalid_instance(self):
        status = self.api.status("feta.discourse.org")
        self.assertFalse(status)
