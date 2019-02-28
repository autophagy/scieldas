from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class Chrome(ServiceAPI):
    base_url = "https://chrome.google.com/webstore/detail/"
    deserializer = "html"

    @ServiceAPI.call
    def version(self, app: str, api: API) -> Optional[str]:
        soup = api.add(app).get(params={"hl": "en-GB"})
        return soup.find("meta", itemprop="version").get("content")

    @ServiceAPI.call
    def users(self, app: str, api: API) -> Optional[str]:
        soup = api.add(app).get(params={"hl": "en-GB"})
        user_string = soup.find("span", {"class": "e-f-ih"}).get("title")
        return user_string.replace(" users", "")

    @ServiceAPI.call
    def rating(self, app: str, api: API) -> Optional[float]:
        soup = api.add(app).get(params={"hl": "en-GB"})
        rating_string = soup.find("meta", itemprop="ratingValue").get("content")
        if rating_string is None:
            return None
        else:
            return round(float(rating_string), 1)
