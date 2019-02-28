from functools import reduce
from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class Jenkins(ServiceAPI):
    base_url = "https://stats.jenkins.io/"
    suffix = ".stats.json"

    @ServiceAPI.call
    def installs(self, plugin: str, api: API, version: str = None) -> Optional[int]:
        plugin_installs = api.add("plugin-installation-trend", plugin).get()
        installations = plugin_installs.get("installationsPerVersion", {})
        if version:
            return installations.get(version)
        else:
            return reduce(lambda x, v: x + v, installations.values(), 0)
