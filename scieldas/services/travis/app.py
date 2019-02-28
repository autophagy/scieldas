from flask import current_app
from scieldas.services import Service
from scieldas.shields import StateShield

from .api import Travis

api = Travis()


class BuildStatus(Service):
    name = "Travis CI Build Status"
    shield = StateShield(
        {"pass": "Passing", "building": "Building", "fail": "Failing"}, prefix="Build"
    )
    base = "travis"
    routes = ["build/:user/:project", "build/:user/:project/:branch"]

    def route(self, user, project, branch=None):
        return api.build_status(
            user, project, current_app.config.get("TRAVIS_API_KEY"), branch=branch
        )
