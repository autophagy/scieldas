from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class NPMRegistry(ServiceAPI):
    base_url = "https://registry.npmjs.org/"

    @ServiceAPI.call
    def license(self, package: str, api: API) -> Optional[str]:
        package_info = api.add(package).get()
        return package_info.get("license")

    @ServiceAPI.call
    def version(self, package: str, api: API) -> Optional[str]:
        version_info = api.add("-", "package", package, "dist-tags").get()
        return version_info.get("latest")


class NPM(ServiceAPI):
    base_url = "https://api.npmjs.org/"

    @ServiceAPI.call
    def downloads(self, period: str, package: str, api: API) -> Optional[str]:
        periods = {"year": "last-year", "month": "last-month", "week": "last-week"}
        point = "1970-1-1:3970-1-1" if period == "total" else periods.get(period, "")
        downloads = api.add("downloads", "point", point, package).get()
        return downloads.get("downloads")
