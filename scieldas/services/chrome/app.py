from scieldas.services import Service
from scieldas.shields import RatingShield, TextShield

from .api import Chrome

api = Chrome()


class Version(Service):
    name = "Chrome Web Store Version"
    example = "2.0.4"
    shield = TextShield(prefix="Version")
    base = "chrome"
    routes = ["version/:appId"]

    def route(self, appId):
        return api.version(appId)


class Users(Service):
    name = "Chrome Web Store Users"
    example = 1380
    shield = TextShield(prefix="Users")
    base = "chrome"
    routes = ["users/:appId"]

    def route(self, appId):
        return api.users(appId)


class Rating(Service):
    name = "Chrome Web Store Rating"
    example = 4.2
    shield = TextShield(prefix="Rating")
    base = "chrome"
    routes = ["rating/:appId"]

    def route(self, appId):
        return api.rating(appId)


class RatingStars(Service):
    name = "Chrome Web Store Rating"
    example = 4.0
    shield = RatingShield(prefix="Rating", min=0, max=5)
    base = "chrome"
    routes = ["rating/stars/:appId"]

    def route(self, appId):
        return api.rating(appId)
