from typing import Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class Crates(ServiceAPI):
    base_url = "https://crates.io/api/v1/crates/"

    @ServiceAPI.call
    def downloads(self, crate: str, api: API, version: str = None) -> Optional[int]:
        if version:
            crate_info = api.add(crate, version).get()
            return get(crate_info, "version.downloads")
        else:
            crate_info = api.add(crate).get()
            return get(crate_info, "crate.downloads")

    @ServiceAPI.call
    def version(self, crate: str, api: API) -> Optional[str]:
        crate_info = api.add(crate).get()
        return get(crate_info, "crate.max_version")
