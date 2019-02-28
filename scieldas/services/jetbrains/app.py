from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Jetbrains

api = Jetbrains()


class Downloads(Service):
    name = "Plugin Downloads"
    shield = TextShield(prefix="Downloads")
    base = "jetbrains"
    example = 10345
    routes = ["build/:pluginId"]

    def route(self, pluginId):
        return api.downloads(pluginId)


class Version(Service):
    name = "Plugin Version"
    shield = TextShield(prefix="Version")
    base = "jetbrains"
    example = "2019.1.5"
    routes = ["version/:pluginId"]

    def route(self, pluginId):
        return api.version(pluginId)
