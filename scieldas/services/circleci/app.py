from scieldas.services import Service
from scieldas.shields import TextShield

from .api import CircleCI

api = CircleCI()


class Build(Service):
    name = "Build"
    shield = TextShield(prefix="Build")
    base = "circleci"
    example = "Success"
    routes = ["build/:vcs/:user/:repo", "build/:vcs/:user/:repo/:branch"]

    def route(self, vcs, user, repo, branch=None):
        build = api.build(vcs, user, repo, branch=branch)
        return build.replace("_", " ").title() if build is not None else build
