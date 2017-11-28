Installation
============

Scieldas requires python >= 3.6.


Via The Repo
-------------

To install Scieldas from the repo, you can clone it and set up a clean environment
with ``virtualenv``: ::

    git clone git@github.com:Autophagy/scieldas.git
    cd datarum
    virtualenv .venv -p python3.6
    source .venv/bin/activate

Then, install the ``scieldas`` package: ::

    pip install -e .

Before you start the service, you must get the requisite API keys, which you can
then export to your environment. For example::

    export TRAVIS_API_KEY=travis_key

You can then start the service with ``gunicorn``::

    gunicorn --bind 0.0.0.0:8080 scieldas

The server will then be available on port 8080 on localhost.
