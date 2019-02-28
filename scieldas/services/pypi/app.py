from scieldas.services import Service
from scieldas.shields import TextShield

from .api import PyPi, PyPiStats

api = PyPi()
statsapi = PyPiStats()


class Version(Service):
    name = "PyPi Version"
    example = "0.2.0"
    shield = TextShield(prefix="PyPi")
    base = "pypi"
    routes = ["version/:project"]

    def route(self, project):
        return api.version(project)


class PyVersions(Service):
    name = "PyPi Python Versions"
    example = "3.4, 3.5, 3.6"
    shield = TextShield(prefix="Python")
    base = "pypi"
    routes = ["pyversions/:project"]

    def route(self, project):
        return api.pyversions(project)


class Status(Service):
    name = "PyPi Status"
    example = "Production/Stable"
    shield = TextShield(prefix="Status")
    base = "pypi"
    routes = ["status/:project"]

    def route(self, project):
        return api.status(project)


class Format(Service):
    name = "PyPi Format"
    example = "wheel"
    shield = TextShield(prefix="Format")
    base = "pypi"
    routes = ["format/:project"]

    def route(self, project):
        return api.format(project)


class License(Service):
    name = "PyPi License"
    example = "MIT License"
    shield = TextShield(prefix="License")
    base = "pypi"
    routes = ["license/:project"]

    def route(self, project):
        return api.license(project)


class Downloads(Service):
    name = "PyPi Downloads"
    example = 102
    shield = TextShield(prefix="Downloads")
    base = "pypi"
    routes = ["downloads/:period(day|week|month)/:project"]

    def route(self, period, project):
        return self.Response(
            statsapi.downloads(period, project), {"suffix": f"/{period}"}
        )
