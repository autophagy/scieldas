from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Mastodon

api = Mastodon()


class Users(Service):
    name = "Mastodon Users"
    shield = TextShield(prefix="Users")
    base = "mastodon"
    example = 306391
    routes = ["users/:instance"]

    def route(self, instance):
        return api.users(instance)


class Statuses(Service):
    name = "Mastodon Statuses"
    shield = TextShield(prefix="Statuses")
    base = "mastodon"
    example = 12859684
    routes = ["statuses/:instance"]

    def route(self, instance):
        return api.statuses(instance)


class Domains(Service):
    name = "Mastodon Domains"
    shield = TextShield(prefix="Domains")
    base = "mastodon"
    example = 8795
    routes = ["domains/:instance"]

    def route(self, instance):
        return api.domains(instance)
