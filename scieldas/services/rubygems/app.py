from scieldas.services import Service
from scieldas.shields import TextShield

from .api import RubyGems

api = RubyGems()


class Downloads(Service):
    name = "RubyGems Downloads"
    shield = TextShield(prefix="Downloads")
    base = "rubygems"
    example = 1024
    routes = ["downloads/:gem", "downloads/:gem/:version"]

    def route(self, gem, version=None):
        return api.downloads(gem, version)


class Version(Service):
    name = "RubyGems Version"
    shield = TextShield(prefix="Version")
    base = "rubygems"
    example = "12.0.4"
    routes = ["version/:gem"]

    def route(self, gem):
        return api.version(gem)
