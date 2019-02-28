from scieldas.services import Service
from scieldas.shields import StateShield, TextShield

from .api import Appveyor

api = Appveyor()


class Build(Service):
    name = "Build"
    shield = StateShield({"success": "Passing", "error": "Failing"}, prefix="Build")
    base = "appveyor"
    routes = ["build/:user/:repo", "build/:user/:repo/:branch"]

    def route(self, user, repo, branch=None):
        return api.build(user, repo, branch=branch)


class Tests(Service):
    name = "Tests"
    shield = TextShield(prefix="Tests")
    example = "61 / 9 / 2"
    base = "appveyor"
    routes = ["tests/:user/:repo", "tests/:user/:repo/:branch"]

    def route(self, user, repo, branch=None):
        results = api.tests(user, repo, branch=branch)
        return " / ".join(
            [str(results.passed), str(results.failed), str(results.skipped)]
        )
