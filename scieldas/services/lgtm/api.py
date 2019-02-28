from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class LGTM(ServiceAPI):
    base_url = "https://lgtm.com/api/v1.0/"

    @ServiceAPI.call
    def alerts(self, owner: str, repo: str, api: API) -> Optional[int]:
        lgtm_details = api.add("projects", "g", owner, repo).get()
        alerts = 0
        for language in lgtm_details.get("languages", []):
            alerts += language.get("alerts", 0)
        return alerts

    @ServiceAPI.call
    def grade(self, language: str, owner: str, repo: str, api: API) -> Optional[str]:
        lgtm_details = api.add("projects", "g", owner, repo).get()
        grade = None
        for l in lgtm_details.get("languages", []):
            if l.get("language") == language:
                grade = l.get("grade")
                break
        return grade
