from scieldas.services import Service
from scieldas.shields import TextShield

from .api import PePy

api = PePy()


class Downloads(Service):
    name = "PePy Total Downloads"
    example = 150000
    shield = TextShield(prefix="Downloads")
    base = "pepy"
    routes = ["downloads/:project"]

    def route(self, project):
        return api.downloads(project)
