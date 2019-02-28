from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Codecov

api = Codecov()


class Coverage(Service):
    name = "Coverage"
    shield = TextShield(prefix="Coverage", suffix="%")
    base = "codecov"
    example = 86.5
    routes = ["coverage/:vcs/:user/:repo", "coverage/:vcs/:user/:repo/:branch"]

    def route(self, vcs, user, repo, branch=None):
        return round(api.coverage(vcs, user, repo, branch=branch), 1)
