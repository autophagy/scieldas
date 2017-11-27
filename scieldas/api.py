import slumber
import os
from collections import defaultdict
import re

API_BASE_URL = {
   'rtd': 'https://readthedocs.org/api/v1/',
   'travis': 'https://api.travis-ci.org/',
   'pypi': 'https://pypi.python.org/pypi/',
   'dockerhub': 'https://hub.docker.com/v2/'
}

BUTTON_BASE_TEXT = {
    'rtd': 'Docs :: {}',
    'travis': 'Build :: {}',
    'pypi version': 'PyPi :: {}',
    'pypi pyversions': 'Python :: {}',
    'dockerhub': 'Docker :: {}',
}

def _create_api(key, append_slash=False):
    return slumber.API(base_url=API_BASE_URL[key], append_slash=append_slash)

def _format_pyversions(classifiers):
    # Pyversions will come in the format 'Programming Language :: Python :: 3.6'
    pattern = '^Programming Language :: Python :: ([\d.]+)$'
    versions = []

    for classifer in classifiers:
        match = re.search(pattern, classifer)
        if match and match.group(1):
            versions.append(match.group(1))

    # Only show major versions if no major.minor appears

    versions = list(filter(lambda x: x not in ['2', '3'], versions))
    return ', '.join(versions)

def get_rtd_build_status(project):
    try:
        api = _create_api('rtd')
        rtd_status = api.version(project).get(slug="latest")

        if len(rtd_status['objects']) > 0:
            if rtd_status['objects'][0]['built']:
                return BUTTON_BASE_TEXT['rtd'].format('Passing')
            else:
                return BUTTON_BASE_TEXT['rtd'].format('Failing')
        else:
            return BUTTON_BASE_TEXT['rtd'].format('Unknown')
    except slumber.exceptions.HttpNotFoundError:
        return BUTTON_BASE_TEXT['rtd'].format('Unknown')

def get_travis_build_status(user, project):
    try:
        api = _create_api('travis')
        user_api = getattr(api.repos, user)
        token = os.environ['TRAVIS_API_KEY']
        travis_project = user_api(project) \
            .get(headers={'Authorization':'token {}'.format(token)})

        if travis_project['last_build_status'] == 0:
            return BUTTON_BASE_TEXT['travis'].format('Passing')
        elif travis_project['last_build_status'] == 1:
            return BUTTON_BASE_TEXT['travis'].format('Failing')
        else:
            return BUTTON_BASE_TEXT['travis'].format('Unknown')
    except slumber.exceptions.HttpNotFoundError:
        return BUTTON_BASE_TEXT['travis'].format('Unknown')

def get_pypi_version(project):
    try:
        api = _create_api('pypi')
        pypi_project = getattr(api, project)
        pypi_json = pypi_project('json').get()

        return BUTTON_BASE_TEXT['pypi version'].format(pypi_json['info']['version'])
    except slumber.exceptions.HttpNotFoundError:
        return BUTTON_BASE_TEXT['pypi version'].format("Unknown")


def get_pypi_pyversions(project):
    try:
        api = _create_api('pypi')
        pypi_project = getattr(api, project)
        pypi_json = pypi_project('json').get()

        classifiers = pypi_json['info']['classifiers']
        return BUTTON_BASE_TEXT['pypi pyversions'].format(_format_pyversions(classifiers))
    except slumber.exceptions.HttpNotFoundError:
        return BUTTON_BASE_TEXT['pypi pyversions'].format("Unknown")

def get_docker_build_status(user, project):
    try:
        api = _create_api('dockerhub')
        user_api = getattr(api.repositories, user)
        latest_builds = user_api(project).buildhistory.get()

        latest_build_result = latest_builds['results'][0]['status']
        if latest_build_result == 10:
            return BUTTON_BASE_TEXT['dockerhub'].format('Passing')
        elif latest_build_result < 0:
            return BUTTON_BASE_TEXT['dockerhub'].format('Failing')
        else:
            return BUTTON_BASE_TEXT['dockerhub'].format('Building')
    except slumber.exceptions.HttpNotFoundError:
        return BUTTON_BASE_TEXT['dockerhub'].format('Unknown')

def get_license(license):
    licenses = defaultdict(lambda: 'Unknown', {'apache': 'Apache 2',
                                               'gpl': 'GPL 3',
                                               'mit': 'MIT'})
    return licenses[license.lower()]
