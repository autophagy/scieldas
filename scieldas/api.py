import slumber
import os
from collections import defaultdict

API_BASE_URL = {
   'rtd': 'http://readthedocs.org/api/v1/',
   'travis': 'https://api.travis-ci.org/',
   'pypi': 'https://pypi.python.org/pypi/',
}

BUTTON_BASE_TEXT = {
    'rtd': 'Docs :: {}',
    'travis': 'Build :: {}',
    'pypi version': 'PyPi :: {}',
    'pypi pyversions': 'Python :: {}',
}

def _create_api(key, append_slash=False):
    return slumber.API(base_url=API_BASE_URL[key], append_slash=append_slash)

def get_rtd_build_status(project):
    api = _create_api('rtd')
    rtd_status = api.version(project).get(slug="latest")

    if rtd_status['objects'][0]['built']:
        return BUTTON_BASE_TEXT['rtd'].format('Passing')
    else:
        return BUTTON_BASE_TEXT['rtd'].format('Failing')

def get_travis_build_status(user, project):
    api = _create_api('travis')
    user_api = getattr(api.repos, user)
    token = os.environ['TRAVIS_API_KEY']
    travis_project = user_api(project) \
        .get(headers={'Authorization':'token {}'.format(token)})

    if travis_project['last_build_status'] == 0:
        return BUTTON_BASE_TEXT['travis'].format('Passing')
    else:
        return BUTTON_BASE_TEXT['travis'].format('Failing')

def get_pypi_version(project):
    api = _create_api('pypi')
    pypi_project = getattr(api, project)
    pypi_json = pypi_project('json').get()

    return BUTTON_BASE_TEXT['pypi version'].format(pypi_json['info']['version'])

def get_pypi_pyversions():
    return True

def get_license(license):
    licenses = defaultdict(lambda: 'Unknown', {'apache': 'Apache 2',
                                               'gpl': 'GPL 3',
                                               'mit': 'MIT'})
    return licenses[license]
