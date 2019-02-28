from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class RubyGems(ServiceAPI):
    base_url = "https://rubygems.org/api/v1/"
    suffix = ".json"

    @ServiceAPI.call
    def downloads(self, gem: str, api: API, version: str = None) -> Optional[int]:
        if version:
            gem_versions = api.add("versions", gem).get()
            for v in gem_versions:
                if v.get("number") == version:
                    return v.get("downloads_count")
        else:
            gem_info = api.add("gems", gem).get()
            return gem_info.get("downloads")
        return None

    @ServiceAPI.call
    def version(self, gem: str, api: API) -> Optional[str]:
        gem_info = api.add("gems", gem).get()
        return gem_info.get("version")
