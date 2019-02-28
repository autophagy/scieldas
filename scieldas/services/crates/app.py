from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Crates

api = Crates()


class Downloads(Service):
    name = "Crates.io Downloads"
    shield = TextShield(prefix="Downloads")
    base = "crates"
    example = 12937998
    routes = ["downloads/:crate", "downloads/:crate/:version"]

    def route(self, crate, filetype, version=None):
        return api.downloads(crate, version)


class Version(Service):
    name = "Crates.io Version"
    shield = TextShield(prefix="Version")
    base = "crates"
    example = "0.2.50"
    routes = ["version/:crate"]

    def route(self, crate):
        return api.version(crate)
