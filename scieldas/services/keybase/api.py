from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class Keybase(ServiceAPI):
    base_url = "https://keybase.io/_/api/1.0/"
    suffix = ".json"

    @ServiceAPI.call
    def pgp(self, username: str, api: API) -> Optional[str]:
        search_results = api.add("user", "lookup").get(params={"usernames": username})
        keybase_user = search_results.get("them", [None])[0]
        if not keybase_user:
            return None
        return (
            keybase_user.get("public_keys", {})
            .get("primary", {})
            .get("key_fingerprint")
        )
