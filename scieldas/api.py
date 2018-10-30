import slumber
import os
import re

from .button import StateButton, TextButton
from .descriptor import Descriptor

API_BASE_URL = {
    "rtd": "https://readthedocs.org/api/v1/",
    "travis": "https://api.travis-ci.org/",
    "pypi": "https://pypi.python.org/pypi/",
    "dockerhub": "https://hub.docker.com/v2/",
}

buttons = {
    "rtd": StateButton({"pass": "Passing", "fail": "Failing"}, prefix="Docs"),
    "travis": StateButton({"pass": "Passing", "fail": "Failing"}, prefix="Build"),
    "dockerhub": StateButton(
        {"pass": "Passing", "fail": "Failing", "building": "Building"}, prefix="Docker"
    ),
    "pypi_version": TextButton(prefix="PyPI"),
    "pypi_pyversions": TextButton(prefix="Python"),
    "licenses": StateButton({"mit": "MIT", "apache": "Apache 2", "gpl": "GPL 3"}),
    "styles": StateButton(
        {"black": "Black", "yapf": "Yapf", "autopep8": "AutoPEP8"}, prefix="Style"
    ),
}

descriptors = {
    "rtd": Descriptor("ReadTheDocs Build Status", "rtd/<project>.svg", buttons["rtd"]),
    "travis": Descriptor(
        "Travis CI Build Status", "travis/<user>/<project>.svg", buttons["travis"]
    ),
    "dockerhub": Descriptor(
        "Docker Hub Build Status",
        "dockerhub/build/<user>/<project>.svg",
        buttons["dockerhub"],
    ),
    "pypi_version": Descriptor(
        "PyPI Version",
        "pypi/version/<project>.svg",
        buttons["pypi_version"],
        example="0.2.0",
    ),
    "pypi_pyversions": Descriptor(
        "PyPI Python Versions",
        "pypi/pyversions/<project>.svg",
        buttons["pypi_pyversions"],
        example="3.6",
    ),
    "licenses": Descriptor("Licenses", "licenses/<license>.svg", buttons["licenses"]),
    "styles": Descriptor("Code Styles", "styles/<style>.svg", buttons["styles"]),
}


def _create_api(key, append_slash=False):
    return slumber.API(base_url=API_BASE_URL[key], append_slash=append_slash)


def _format_pyversions(classifiers):
    # Pyversions will come in the format 'Programming Language :: Python :: 3.6'
    pattern = "^Programming Language :: Python :: ([\d.]+)$"
    versions = []

    for classifer in classifiers:
        match = re.search(pattern, classifer)
        if match and match.group(1):
            versions.append(match.group(1))

    # Only show major versions if no major.minor appears

    versions = list(filter(lambda x: x not in ["2", "3"], versions))
    return ", ".join(versions)


def get_rtd_build_status(project):
    try:
        api = _create_api("rtd")
        rtd_status = api.version(project).get(slug="latest")
        button = buttons["rtd"]

        if len(rtd_status["objects"]) > 0:
            if rtd_status["objects"][0]["built"]:
                return button.create("pass")
            else:
                return button.create("fail")
        else:
            return button.create()
    except slumber.exceptions.HttpNotFoundError:
        return button.create()


def get_travis_build_status(user, project):
    try:
        api = _create_api("travis")
        user_api = getattr(api.repos, user)
        token = os.environ["TRAVIS_API_KEY"]
        travis_project = user_api(project).get(
            headers={"Authorization": "token {}".format(token)}
        )
        button = buttons["travis"]

        if travis_project["last_build_status"] == 0:
            return button.create("pass")
        elif travis_project["last_build_status"] == 1:
            return button.create("fail")
        else:
            return button.create()
    except slumber.exceptions.HttpNotFoundError:
        return button.create()


def get_pypi_version(project):
    try:
        api = _create_api("pypi")
        pypi_project = getattr(api, project)
        pypi_json = pypi_project("json").get()
        button = buttons["pypi_version"]

        return button.create(pypi_json["info"]["version"])
    except slumber.exceptions.HttpNotFoundError:
        return button.create()


def get_pypi_pyversions(project):
    try:
        api = _create_api("pypi")
        pypi_project = getattr(api, project)
        pypi_json = pypi_project("json").get()
        button = buttons["pypi_pyversions"]

        classifiers = pypi_json["info"]["classifiers"]
        return button.create(_format_pyversions(classifiers))
    except slumber.exceptions.HttpNotFoundError:
        return button.create()


def get_docker_build_status(user, project):
    try:
        api = _create_api("dockerhub")
        user_api = getattr(api.repositories, user)
        latest_builds = user_api(project).buildhistory.get()
        button = buttons["dockerhub"]

        latest_build_result = latest_builds["results"][0]["status"]
        if latest_build_result == 10:
            return button.create("pass")
        elif latest_build_result < 0:
            return button.create("fail")
        else:
            return button.create("building")
    except slumber.exceptions.HttpNotFoundError:
        return button.create()


def get_license(license):
    button = buttons["licenses"]
    return button.create(license)


def get_code_style(style):
    button = buttons["styles"]
    return button.create(style)
