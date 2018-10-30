from flask import Flask, make_response, abort, render_template
from functools import wraps

application = Flask(__name__)

from . import api
from . import image_creator


def create_image_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            image, filetype = func(*args, **kwargs)
            if filetype == "svg":
                response = make_response(image.tostring())
                response.content_type = "image/svg+xml"
            else:
                response = make_response(image)
                response.content_type = "image/png"
            response.cache_control.max_age = 60
            return response
        except ValueError:
            abort(404)

    return wrapper


@application.route("/")
def index():
    return render_template("index.html", descriptors=api.descriptors)


# Read The Docs
@application.route("/rtd/<project>.<filetype>")
@create_image_response
def rtd(project, filetype):
    return (
        image_creator.create_image(filetype, api.get_rtd_build_status, project),
        filetype,
    )


# Travis
@application.route("/travis/<user>/<project>.<filetype>")
@create_image_response
def travis(user, project, filetype):
    return (
        image_creator.create_image(
            filetype, api.get_travis_build_status, user, project
        ),
        filetype,
    )


# PyPi
@application.route("/pypi/version/<project>.<filetype>")
@create_image_response
def pypi_version(project, filetype):
    return image_creator.create_image(filetype, api.get_pypi_version, project), filetype


@application.route("/pypi/pyversions/<project>.<filetype>")
@create_image_response
def pyversions(project, filetype):
    return (
        image_creator.create_image(filetype, api.get_pypi_pyversions, project),
        filetype,
    )


# Dockerhub


@application.route("/dockerhub/build/<user>/<project>.<filetype>")
@create_image_response
def docker_build(user, project, filetype):
    return (
        image_creator.create_image(
            filetype, api.get_docker_build_status, user, project
        ),
        filetype,
    )


# Licenses
@application.route("/licenses/<license>.<filetype>")
@create_image_response
def licenses(license, filetype):
    return image_creator.create_image(filetype, api.get_license, license), filetype


# Code Styles
@application.route("/styles/<style>.<filetype>")
@create_image_response
def code_styles(style, filetype):
    return image_creator.create_image(filetype, api.get_code_style, style), filetype


@application.route("/_/health", methods=["GET"])
def health_check():
    return "OK"


if __name__ == "__main__":
    application.run(host="0.0.0.0")
