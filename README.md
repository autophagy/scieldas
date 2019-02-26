# Scieldas

[![Documentation Status](https://scieldas.autophagy.io/rtd/scieldas.png)](https://scieldas.readthedocs.io/en/latest)
[![Docker Build Status](https://scieldas.autophagy.io/dockerhub/build/autophagy/scieldas.png)](https://hub.docker.com/r/autophagy/scieldas/)
[![Black](https://scieldas.autophagy.io/styles/black.png)](https://black.readthedocs.io/en/stable/)
[![MIT License](https://scieldas.autophagy.io/licenses/MIT.png)](LICENSE)

[Scieldas](https://scieldas.autophagy.io) is a service to provide metadata badges for open source project
READMEs, inspired by [Shields.io](https://shields.io). It currently supports:

  - **Read The Docs** :: Build status of the Latest tag.
  - **Travis CI** :: Build status of the last build.
  - **PyPI** :: Version of project and supported python versions.
  - **Docker Hub** :: Status of the latest build.
  - **Licenses** :: The license of the project.
  - **Styles** :: The autoformatted code style of the project.

Built with Flask and Docker.

## Running Scieldas

Running the Scieldas service requires [Docker](https://www.docker.com). You can either build
it yourself:

    $ docker build -t "autophagy:scieldas" .
    $ docker run -d --name=scieldas -p 80:8080 --env TRAVIS_API_KEY=key autophagy:scieldas

Or pull the image from [Docker Hub](https://hub.docker.com/r/autophagy/scieldas/) :

    $ docker pull autophagy/scieldas
    $ docker run -d --name=scieldas -p 80:8080 --env TRAVIS_API_KEY=key autophagy/scieldas

For more detailed information, including reqiured API keys, please see
the [documentation](https://scieldas.readthedocs.io/en/latest/).

## Supported Badges

### Travis CI

![Travis Build Passing](seonu/_static/travis/Build-Passing.png)
![Travis Build Failing](seonu/_static/travis/Build-Failing.png)
![Travis Build Unknown](seonu/_static/travis/Build-Unknown.png)

### Read The Docs

![Read The Docs Build Passing](seonu/_static/rtd/Docs-Passing.png)
![Read The Docs Build Failing](seonu/_static/rtd/Docs-Failing.png)
![Read The Docs Build Unknown](seonu/_static/rtd/Docs-Unknown.png)

### Coveralls

![Coveralls Coverage](seonu/_static/coveralls/Coveralls.png)

### PyPI

#### Version

![PyPI Version](seonu/_static/pypi/Pypi-Version.png)

#### Python Versions

![Python Versions](seonu/_static/pypi/Python-Versions.png)

### PePy Downloads

![PePy Downloads](seonu/_static/pepy/PePy-Downloads.png)

### Docker Hub

![Docker Build Passing](seonu/_static/dockerhub/Build-Passing.png)
![Docker Build Failing](seonu/_static/dockerhub/Build-Failing.png)
![Docker Build Building](seonu/_static/dockerhub/Build-Building.png)
![Docker Build Unknown](seonu/_static/dockerhub/Build-Unknown.png)

### Licenses

![Apache 2.0 license](seonu/_static/licenses/Apache.png)
![GPL license](seonu/_static/licenses/GPL.png)
![MIT license](seonu/_static/licenses/MIT.png)

### Code Styles

![Black](seonu/_static/styles/black.png)
![Yapf](seonu/_static/styles/yapf.png)
![AutoPEP8](seonu/_static/styles/autopep8.png)
