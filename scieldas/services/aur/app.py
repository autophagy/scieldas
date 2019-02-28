from scieldas.services import Service
from scieldas.shields import TextShield

from .api import AUR

api = AUR()


class Version(Service):
    name = "Arch User Repository Version"
    example = "3.3.0-1"
    shield = TextShield(prefix="Version")
    base = "aur"
    routes = ["version/:package"]

    def route(self, package):
        return api.version(package)


class License(Service):
    name = "Arch User Repository License"
    example = "Apache"
    shield = TextShield(prefix="License")
    base = "aur"
    routes = ["license/:package"]

    def route(self, package):
        return api.license(package)


class Votes(Service):
    name = "Arch User Repository Votes"
    example = "75"
    shield = TextShield(prefix="Votes")
    base = "aur"
    routes = ["votes/:package"]

    def route(self, package):
        return api.votes(package)
