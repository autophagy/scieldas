from scieldas.services import Service
from scieldas.shields import StateShield, TextShield

from .api import DockerHub

api = DockerHub()


class BuildStatus(Service):
    name = "Docker Hub Build Status"
    shield = StateShield(
        {"pass": "Passing", "fail": "Failing", "building": "Building"}, prefix="Docker"
    )
    base = "dockerhub"
    routes = ["build/:user/:project"]

    def route(self, user, project):
        return api.build_status(user, project)


class Pulls(Service):
    name = "Docker Hub Pull Count"
    example = 6021
    shield = TextShield(prefix="Pulls")
    base = "dockerhub"
    routes = ["pulls/:user/:project"]

    def route(self, user, project):
        return api.pulls(user, project)


class Stars(Service):
    name = "Docker Hub Star Count"
    example = 113
    shield = TextShield(prefix="Stars")
    base = "dockerhub"
    routes = ["stars/:user/:project"]

    def route(self, user, project):
        return api.stars(user, project)
