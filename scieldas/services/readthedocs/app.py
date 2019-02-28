from scieldas.services import Service
from scieldas.shields import StateShield

from .api import ReadTheDocs

api = ReadTheDocs()


class BuildStatus(Service):
    name = "ReadTheDocs Build Status"
    shield = StateShield({"pass": "Passing", "fail": "Failing"}, prefix="Docs")
    base = "rtd"
    routes = ["build/:project", "build/:project/:version"]

    def route(self, project, version=None):
        return api.build_status(project, version=version)
