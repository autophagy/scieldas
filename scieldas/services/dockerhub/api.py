from typing import Optional

from scieldas.api import API
from scieldas.services import ServiceAPI


class DockerHub(ServiceAPI):
    base_url = "https://hub.docker.com/v2/"

    @ServiceAPI.call
    def build_status(self, user: str, project: str, api: API) -> Optional[str]:
        latest_builds = api.add("repositories", user, project, "buildhistory").get()
        latest_build_result = latest_builds["results"][0]["status"]
        if latest_build_result == 10:
            return "pass"
        elif latest_build_result < 0:
            return "fail"
        else:
            return "building"

    @ServiceAPI.call
    def pulls(self, user: str, project: str, api: API) -> Optional[int]:
        project_info = api.add("repositories", user, project).get()
        return project_info.get("pull_count")

    @ServiceAPI.call
    def stars(self, user: str, project: str, api: API) -> Optional[int]:
        project_info = api.add("repositories", user, project).get()
        return project_info.get("star_count")
