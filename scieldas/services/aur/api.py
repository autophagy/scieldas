from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class AUR(ServiceAPI):
    base_url = "https://aur.archlinux.org/rpc/"

    @ServiceAPI.call
    def version(self, package: str, api: API) -> Optional[str]:
        package_info = api.get(params={"v": "5", "type": "info", "arg[]": package})
        if len(package_info["results"]) == 0:
            return None
        return package_info["results"][0].get("Version")

    @ServiceAPI.call
    def license(self, package: str, api: API) -> Optional[str]:
        package_info = api.get(params={"v": "5", "type": "info", "arg[]": package})
        if len(package_info["results"]) == 0:
            return None
        return package_info["results"][0].get("License")[0]

    @ServiceAPI.call
    def votes(self, package: str, api: API) -> Optional[str]:
        package_info = api.get(params={"v": "5", "type": "info", "arg[]": package})
        if len(package_info["results"]) == 0:
            return None
        return package_info["results"][0].get("NumVotes")
