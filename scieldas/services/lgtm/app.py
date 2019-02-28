from scieldas.services import Service
from scieldas.shields import TextShield

from .api import LGTM

api = LGTM()


class Alerts(Service):
    name = "LGTM Alerts"
    shield = TextShield(prefix="LGTM", suffix=" Alerts")
    base = "lgtm"
    example = 104
    routes = ["alerts/:owner/:repo"]

    def route(self, owner, repo):
        return api.alerts(owner, repo)


class Grade(Service):
    name = "LGTM Grade"
    shield = TextShield(prefix="LGTM")
    base = "lgtm"
    example = "A+"
    routes = ["grade/:language/:owner/:repo"]

    def route(self, language, owner, repo):
        return self.Response(
            api.grade(language, owner, repo),
            {"prefix": f"LGTM {language.capitalize()}"},
        )
