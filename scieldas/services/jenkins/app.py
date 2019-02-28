from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Jenkins

api = Jenkins()


class Installs(Service):
    name = "Jenkins Plugin Installs"
    example = 72931
    shield = TextShield(prefix="Installs")
    base = "jenkins"
    routes = ["installs/:plugin", "installs/:plugin/:version"]

    def route(self, plugin, version=None):
        prefix = f" Installs ({version})" if version else None
        return self.Response(
            content=api.installs(plugin, version=version), params={"prefix": prefix}
        )
