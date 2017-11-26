from flask import Flask, make_response, redirect
application = Flask(__name__)

from . import api
from . import svg_creator


def create_svg_response(svg):
    response = make_response(svg.tostring())
    response.content_type = 'image/svg+xml'
    return response

@application.route("/")
def index():
    return redirect("https://github.com/autophagy/scieldas", code=302)

# Read The Docs
@application.route("/rtd/<project>.svg")
def rtd(project):
    svg = svg_creator.create_svg(api.get_rtd_build_status, project)
    return create_svg_response(svg)

# Travis
@application.route("/travis/<user>/<project>.svg")
def travis(user, project):
    svg = svg_creator.create_svg(api.get_travis_build_status, user, project)
    return create_svg_response(svg)

# PyPi
@application.route("/pypi/version/<project>.svg")
def pypi_version(project):
    svg = svg_creator.create_svg(api.get_pypi_version, project)
    return create_svg_response(svg)

@application.route("/pypi/pyversions/<project>.svg")
def pyversions(project):
    svg = svg_creator.create_svg(api.get_pypi_pyversions, project)
    return create_svg_response(svg)

# Licenses
@application.route("/licenses/<license>.svg")
def licenses(license):
    svg = svg_creator.create_svg(api.get_license, license)
    return create_svg_response(svg)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
