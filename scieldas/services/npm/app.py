from scieldas.services import Service
from scieldas.shields import TextShield

from .api import NPM, NPMRegistry

registry_api = NPMRegistry()
api = NPM()


class Version(Service):
    name = "NPM Version"
    example = "2.0.1"
    shield = TextShield(prefix="Version")
    base = "npm"
    routes = ["version/:package"]

    def route(self, package):
        return registry_api.version(package)


class License(Service):
    name = "NPM License"
    example = "Apache-2.0"
    shield = TextShield(prefix="License")
    base = "npm"
    routes = ["license/:package"]

    def route(self, package):
        return registry_api.license(package)


class Downloads(Service):
    name = "NPM Downloads"
    example = 870_355_472
    shield = TextShield(prefix="Downloads")
    base = "npm"
    routes = ["downloads/:period(total|year|month|week/:package"]

    def route(self, period, package):
        downloads = api.downloads(period, package)
        if period != "total":
            return self.Response(downloads, {"suffix": f"/{period}"})
        return downloads
