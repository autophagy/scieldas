from flask import Flask
app = Flask(__name__)

import slumber
import svgwrite

def generate_svg(text):

    # Width is our twice our padding (2*16) plus 7 pixels per character
    svg = svgwrite.Drawing(size = ("{}px".format((len(text)*7)+32), "41px"))
    text_style = ("font-size: 14px; "
                  "font-family: Inconsolata, monospace;"
                  "text-align: center")
    scield_rect = svg.rect(size=('100%', '100%'), fill='#2D2D2D')
    scield_text = svg.text(text, insert=(16, 24), fill="#F2F2F2", style=text_style)

    svg.add(scield_rect)
    svg.add(scield_text)
    return svg.tostring()


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

    return(generate_svg("Docs :: {}".format(
        built_map[v['objects'][0]['built']])))

# Travis
@app.route("/travis/<project>")
def travis(project):
    return("<h1>Travis</h1>\n"
           "<p>Return Travis build status for :: {}".format(project))

# PyPi
@app.route("/pypi/version/<project>.svg")
def pypi_version(project):

    api = slumber.API(base_url='https://pypi.python.org/pypi/')
    api_to_call = getattr(api, project)
    v = api_to_call('json').get()

    return(generate_svg("PyPi :: {}".format(v['info']['version'])))

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
