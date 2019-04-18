import re
from typing import List, Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class PyPi(ServiceAPI):
    base_url = "https://pypi.python.org/pypi/"

    @ServiceAPI.call
    def version(self, project: str, api: API) -> Optional[str]:
        pypi_json = api.add(project, "json").get()
        return get(pypi_json, "info.version")

    @staticmethod
    def _format_pyversions(classifiers: List[str]) -> str:
        # Pyversions will come in the format 'Programming Language :: Python :: 3.6'
        pattern = r"^Programming Language :: Python :: ([\d.]+)$"
        versions = []

        for classifer in classifiers:
            match = re.search(pattern, classifer)
            if match and match.group(1):
                versions.append(match.group(1))

        # Only show major versions if no major.minor appears

        versions = list(filter(lambda x: x not in ["2", "3"], versions))
        return ", ".join(versions)

    @ServiceAPI.call
    def pyversions(self, project: str, api: API) -> Optional[str]:
        pypi_json = api.add(project, "json").get()
        classifiers = self._format_pyversions(pypi_json["info"]["classifiers"])
        if len(classifiers) > 0:
            return classifiers
        else:
            return None

    @staticmethod
    def _format_status(classifiers: List[str]) -> Optional[str]:
        """
        According to https://pypi.org/pypi?%3Aaction=list_classifiers
        the following are valid statuses:

        Development Status :: 1 - Planning
        Development Status :: 2 - Pre-Alpha
        Development Status :: 3 - Alpha
        Development Status :: 4 - Beta
        Development Status :: 5 - Production/Stable
        Development Status :: 6 - Mature
        Development Status :: 7 - Inactive
        """
        pattern = r"^Development Status :: \d - (.*)$"
        statuses = [
            "Planning",
            "Pre-Alpha",
            "Alpha",
            "Beta",
            "Production/Stable",
            "Mature",
            "Inactive",
        ]

        for classifier in classifiers:
            match = re.search(pattern, classifier)
            if match and match.group(1) and match.group(1) in statuses:
                return match.group(1)
        return None

    @ServiceAPI.call
    def status(self, project: str, api: API) -> Optional[str]:
        pypi_json = api.add(project, "json").get()
        return self._format_status(pypi_json["info"]["classifiers"])

    @staticmethod
    def _get_package_format(releaseArtifacts: List[dict]) -> str:
        wheel = ["wheel", "bdist_wheel"]
        egg = ["egg", "bdist_egg"]
        has_wheel, has_egg = False, False
        for artifact in releaseArtifacts:
            has_wheel = artifact["packagetype"] in wheel or has_wheel
            has_egg = artifact["packagetype"] in egg or has_egg
        return "wheel" if has_wheel else "egg" if has_egg else "source"

    @ServiceAPI.call
    def format(self, project: str, api: API) -> Optional[str]:
        pypi_json = api.add(project, "json").get()
        version = pypi_json["info"]["version"]
        return self._get_package_format(pypi_json["releases"][version])

    @staticmethod
    def _format_license(classifiers: List[str]) -> Optional[str]:
        pattern = re.compile(r"^License :: (.+)$")

        for classifier in classifiers:
            match = pattern.search(classifier)
            if match and match.group(1):
                return match.group(1).split(" :: ")[-1]
        return None

    @ServiceAPI.call
    def license(self, project: str, api: API) -> Optional[str]:
        pypi_json = api.add(project, "json").get()
        return self._format_license(get(pypi_json, "info.classifiers"))


class PyPiStats(ServiceAPI):
    base_url = "https://pypistats.org/api/"

    @ServiceAPI.call
    def downloads(self, period: str, project: str, api: API) -> Optional[int]:
        periods = {"day": "last_day", "week": "last_week", "month": "last_month"}
        recent_stats = api.add("packages", project, "recent").get()
        return get(recent_stats, f"data.{periods.get(period, period)}")
