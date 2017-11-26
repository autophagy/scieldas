from flask import Flask, make_response
app = Flask(__name__)

import slumber
import svgwrite
from collections import defaultdict
import os

def generate_svg_response(text):

    # Width is our twice our padding (2*16) plus 7 pixels per character
    svg = svgwrite.Drawing(size = ("{}px".format((len(text)*7)+32), "41px"))
    text_style = ("font-size: 14px; "
                  "font-family: Inconsolata, monospace;"
                  "text-align: center")
    scield_rect = svg.rect(size=('100%', '100%'), fill='#2D2D2D')
    scield_text = svg.text(text, insert=(16, 24), fill="#F2F2F2", style=text_style)

    svg.add(scield_rect)
    svg.add(scield_text)

    response = make_response(svg.tostring())
    response.content_type = 'image/svg+xml'
    return response


@app.route("/")
def index():
    return("<h1>Scieldas</h1>\n"
            "<p>Shields for software READMES</p>")

# Read The Docs
@app.route("/rtd/<project>.svg")
def rtd(project):
    api = slumber.API(base_url='http://readthedocs.org/api/v1/')
    v = api.version(project).get(slug="latest")

    built_map = {True: 'Passing', False: 'Failing'}

    return(generate_svg_response("Docs :: {}".format(
        built_map[v['objects'][0]['built']])))

# Travis
@app.route("/travis/<user>/<project>.svg")
def travis(user, project):

    travis_statuses = {0: 'Passing', 1: 'Failing'}
    api = slumber.API(base_url='https://api.travis-ci.org/', append_slash=False)
    api_to_call = getattr(api.repos, user)
    v = api_to_call(project).get(headers={'Authorization':
                                            'token {}'.format(os.environ['TRAVIS_API_KEY'])})

    return (generate_svg_response("Build :: {}".format(travis_statuses[v['last_build_status']])))

# PyPi
@app.route("/pypi/version/<project>.svg")
def pypi_version(project):

    api = slumber.API(base_url='https://pypi.python.org/pypi/')
    api_to_call = getattr(api, project)
    v = api_to_call('json').get()

    return(generate_svg_response("PyPi :: {}".format(v['info']['version'])))

@app.route("/pypi/pyversions/<project>")
def pyversions(project):
    return("<h1>PyPi Python Versions/h1>\n"
           "<p>Return the supported python versions for :: {}".format(project))

# Licenses
@app.route("/licenses/<license>.svg")
def licenses(license):

    licenses = defaultdict(lambda: 'Unknown', {'apache': 'Apache 2',
                                               'gpl': 'GPL 3',
                                               'mit': 'MIT'})

    return(generate_svg_response(licenses[license]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
