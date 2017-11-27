========
Scieldas
========

.. image:: http://scieldas.autophagy.io/dockerhub/build/autophagy/scieldas.svg
   :target: https://hub.docker.com/r/autophagy/scieldas/
   :alt: Docker Build Status

.. image:: http://scieldas.autophagy.io/licenses/MIT.svg
   :target: LICENSE
   :alt: MIT License


Badges for software projects. Aiming to initially support Travis, RTD, PyPi
(version and pyversions) and licenses (Apache, GPL, MIT).

Built with Flask and Docker, probably. `Specification`_.

Running Scieldas
================

Running the Scieldas service requires `Docker`_. You can either build it
yourself::

    $ docker build -t "autophagy:scieldas" .
    $ docker run -d --name=scieldas -p 80:8080 --env TRAVIS_API_KEY=key autophagy:scieldas

Or pull the image from `Docker Hub`_ ::

    $ docker pull autophagy/scieldas
    $ docker run -d --name=scieldas -p 80:8080 --env TRAVIS_API_KEY=key autophagy/scieldas

When running the container, replace the ``key`` in the Travis API env variable
with your own key. To generate a key, see the `Travis API documentation`_.

Button Examples
===============

Read The Docs
-------------

.. image:: spec/examples/rtd/Docs-Passing.png
    :target: _
    :alt: Read The Docs Build Passing

.. image:: spec/examples/rtd/Docs-Failing.png
    :target: _
    :alt: Read The Docs Build Failing

.. image:: spec/examples/rtd/Docs-Unknown.png
    :target: _
    :alt: Read The Docs Build Unknown


Travis
------

.. image:: spec/examples/travis/Build-Passing.png
    :target: _
    :alt: Travis Build Passing

.. image:: spec/examples/travis/Build-Failing.png
    :target: _
    :alt: Travis Build Failing

.. image:: spec/examples/travis/Build-Unknown.png
    :target: _
    :alt: Travis Build Unknown

PyPi
----

.. image:: spec/examples/pypi/Pypi-Version.png
    :target: _
    :alt: PyPi Version

.. image:: spec/examples/pypi/Python-Versions.png
    :target: _
    :alt: Python Versions

Licenses
--------

.. image:: spec/examples/licenses/Apache.png
    :target: _
    :alt: Apache 2.0 license

.. image:: spec/examples/licenses/GPL.png
    :target: _
    :alt: GPL license

.. image:: spec/examples/licenses/MIT.png
    :target: _
    :alt: MIT license

.. _Specification: spec/spec.rst
.. _Docker: https://www.docker.com
.. _Docker Hub: https://hub.docker.com/r/autophagy/scieldas/
.. _Travis API documentation: https://docs.travis-ci.com/api#authentication
