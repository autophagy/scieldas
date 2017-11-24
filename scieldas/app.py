from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return("<h1>Scieldas</h1>\n"
            "<p>Shields for software READMES</p>")

# Read The Docs
@app.route("/rtd/<project>")
def rtd(project):
    return("<h1>Read The Docs</h1>\n"
           "<p>Return RTD build status for :: {}".format(project))

# Travis
@app.route("/travis/<project>")
def travis(project):
    return("<h1>Travis</h1>\n"
           "<p>Return Travis build status for :: {}".format(project))

# PyPi
@app.route("/pypi/version/<project>")
def pypi_version(project):
    return("<h1>PyPi Version</h1>\n"
           "<p>Return latest PyPi version for :: {}".format(project))

@app.route("/pypi/pyversions/<project>")
def pyversions(project):
    return("<h1>PyPi Python Versions/h1>\n"
           "<p>Return the supported python versions for :: {}".format(project))

# Licenses
@app.route("/licenses/<license>")
def licenses(license):
    return("<h1>license</h1>\n"
           "<p>Return license badge for {} license</p>".format(project))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

