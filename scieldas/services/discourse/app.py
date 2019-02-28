from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Discourse

api = Discourse()


class Topics(Service):
    name = "Discourse Topics"
    shield = TextShield(prefix="Topics")
    base = "discourse"
    example = 209
    routes = ["topics/:instance"]

    def route(self, instance):
        return api.topics(instance)


class Users(Service):
    name = "Discourse Users"
    shield = TextShield(prefix="Users")
    base = "discourse"
    example = 209
    routes = ["users/:instance"]

    def route(self, instance):
        return api.users(instance)


class Posts(Service):
    name = "Discourse Posts"
    shield = TextShield(prefix="Posts")
    base = "discourse"
    example = 209
    routes = ["posts/:instance"]

    def route(self, instance):
        return api.posts(instance)


class Likes(Service):
    name = "Discourse Likes"
    shield = TextShield(prefix="Likes")
    base = "discourse"
    example = 209
    routes = ["likes/:instance"]

    def route(self, instance):
        return api.likes(instance)


class Status(Service):
    name = "Discourse Status"
    shield = TextShield(prefix="Status")
    base = "discourse"
    example = "Online"
    routes = ["status/:instance"]

    def route(self, instance):
        return "Online" if api.status(instance) else "Offline"
