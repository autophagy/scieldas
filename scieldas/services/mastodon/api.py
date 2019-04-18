from typing import Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class Mastodon(ServiceAPI):
    base_url = "https://{}/api/v1/"

    @ServiceAPI.call
    def users(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        instance_info = api.add("instance").get()
        return get(instance_info, "stats.user_count")

    @ServiceAPI.call
    def statuses(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        instance_info = api.add("instance").get()
        return get(instance_info, "stats.status_count")

    @ServiceAPI.call
    def domains(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        instance_info = api.add("instance").get()
        return get(instance_info, "stats.domain_count")
