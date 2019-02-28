from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Coveralls

api = Coveralls()


class Coverage(Service):
    name = "Coveralls Test Coverage"
    example = 86.5
    shield = TextShield(prefix="Coverage", suffix="%")
    base = "coveralls"
    routes = ["coverage/:vcs/:user/:project", "coverage/:vcs/:user/:project/:branch"]

    def route(self, vcs, user, project, branch=None):
        return round(api.coverage(vcs, user, project, branch=branch), 1)
