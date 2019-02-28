from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class Mozilla(ServiceAPI):
    base_url = "https://addons.mozilla.org/api/v3/"

    @ServiceAPI.call
    def weekly_downloads(self, addon: str, api: API) -> Optional[str]:
        addon_info = api.add("addons", "addon", addon).get()
        return addon_info.get("weekly_downloads")

    @ServiceAPI.call
    def users(self, addon: str, api: API) -> Optional[str]:
        addon_info = api.add("addons", "addon", addon).get()
        return addon_info.get("average_daily_users")

    @ServiceAPI.call
    def version(self, addon: str, api: API) -> Optional[str]:
        addon_info = api.add("addons", "addon", addon).get()
        return addon_info.get("current_version", {}).get("version")

    @ServiceAPI.call
    def rating(self, addon: str, api: API) -> float:
        addon_info = api.add("addons", "addon", addon).get()
        return addon_info.get("ratings", {}).get("average")
