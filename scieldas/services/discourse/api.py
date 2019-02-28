from typing import Optional

from requests.exceptions import RequestException
from scieldas.api import API
from scieldas.services import ServiceAPI


class Discourse(ServiceAPI):
    base_url = "https://{}/site/"
    suffix = ".json"

    @ServiceAPI.call
    def topics(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        stats = api.add("statistics").get()
        return stats.get("topic_count")

    @ServiceAPI.call
    def users(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        stats = api.add("statistics").get()
        return stats.get("user_count")

    @ServiceAPI.call
    def posts(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        stats = api.add("statistics").get()
        return stats.get("post_count")

    @ServiceAPI.call
    def likes(self, instance: str, api: API) -> Optional[int]:
        api.base_url = self.base_url.format(instance)
        stats = api.add("statistics").get()
        return stats.get("like_count")

    @ServiceAPI.call
    def status(self, instance: str, api: API) -> bool:
        try:
            api.base_url = self.base_url.format(instance)
            stats = api.add("statistics").get()
            return True if stats else False
        except RequestException:
            return False
