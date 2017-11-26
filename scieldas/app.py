from flask import Flask, make_response
app = Flask(__name__)

import api
import svg_creator


def create_svg_response(svg):
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
    svg = svg_creator.create_svg(api.get_rtd_build_status, project)
    return create_svg_response(svg)

# Travis
@app.route("/travis/<user>/<project>.svg")
def travis(user, project):
    svg = svg_creator.create_svg(api.get_travis_build_status, user, project)
    return create_svg_response(svg)

# PyPi
@app.route("/pypi/version/<project>.svg")
def pypi_version(project):
    svg = svg_creator.create_svg(api.get_pypi_version, project)
    return create_svg_response(svg)

@app.route("/pypi/pyversions/<project>.svg")
def pyversions(project):
    svg = svg_creator.create_svg(api.get_pypi_pyversions, project)
    return create_svg_response(svg)

# Licenses
@app.route("/licenses/<license>.svg")
def licenses(license):
    svg = svg_creator.create_svg(api.get_license, license)
    return create_svg_response(svg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
