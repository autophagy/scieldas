from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class ReadTheDocs(ServiceAPI):
    base_url = "https://readthedocs.org/api/v2/"

    @ServiceAPI.call
    def build_status(
        self, project: str, api: API, version: str = None
    ) -> Optional[str]:
        if version is None:
            version = "latest"
        versions = api.add("version").get(
            params={"project__slug": project, "active": True}
        )
        for result in versions.get("results", []):
            if result.get("slug") == version:
                return "pass" if result.get("built") else "fail"
        return None
