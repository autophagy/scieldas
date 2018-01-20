from flask import Flask, make_response, redirect, abort
application = Flask(__name__)

from . import api
from . import image_creator


def create_image_response(image, filetype):
    if filetype == 'svg':
        response = make_response(image.tostring())
        response.content_type = 'image/svg+xml'
    else:
        response = make_response(image)
        response.content_type = 'image/png'
    response.cache_control.max_age = 60
    return response

@application.route("/")
def index():
    return redirect("https://github.com/autophagy/scieldas", code=302)

# Read The Docs
@application.route("/rtd/<project>.<filetype>")
def rtd(project, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_rtd_build_status, project)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

# Travis
@application.route("/travis/<user>/<project>.<filetype>")
def travis(user, project, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_travis_build_status, user, project)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

# PyPi
@application.route("/pypi/version/<project>.<filetype>")
def pypi_version(project, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_pypi_version, project)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

@application.route("/pypi/pyversions/<project>.<filetype>")
def pyversions(project, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_pypi_pyversions, project)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

# Dockerhub

@application.route("/dockerhub/build/<user>/<project>.<filetype>")
def docker_build(user, project, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_docker_build_status, user, project)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

# Licenses
@application.route("/licenses/<license>.<filetype>")
def licenses(license, filetype):
    try:
        img = image_creator.create_image(filetype, api.get_license, license)
        return create_image_response(img, filetype)
    except ValueError:
        abort(404)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
