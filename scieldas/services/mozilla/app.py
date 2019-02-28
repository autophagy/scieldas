from scieldas.services import Service
from scieldas.shields import RatingShield, TextShield

from .api import Mozilla

api = Mozilla()


class WeeklyDownloads(Service):
    name = "Mozilla Add-on Weekly Downloads"
    example = 120
    shield = TextShield(prefix="Downloads", suffix="/week")
    base = "mozilla"
    routes = ["downloads/:addon"]

    def route(self, addon):
        return api.weekly_downloads(addon)


class Users(Service):
    name = "Mozilla Add-on Average Daily Users"
    example = 75
    shield = TextShield(prefix="Users")
    base = "mozilla"
    routes = ["users/:addon"]

    def route(self, addon):
        return api.users(addon)


class Version(Service):
    name = "Mozilla Add-on Version"
    example = "2.0.1"
    shield = TextShield(prefix="Version")
    base = "mozilla"
    routes = ["version/:addon"]

    def route(self, addon):
        return api.version(addon)


class Rating(Service):
    name = "Mozilla Add-on Rating"
    example = 4.2
    shield = TextShield(prefix="Rating")
    base = "mozilla"
    routes = ["rating/:addon"]

    def route(self, addon):
        return api.rating(addon)


class RatingStars(Service):
    name = "Mozilla Add-on Rating"
    example = 4.2
    shield = RatingShield(prefix="Rating", min=0, max=5)
    base = "mozilla"
    routes = ["rating/stars/:addon"]

    def route(self, addon):
        return api.rating(addon)
