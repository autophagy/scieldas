Deployment with Docker
======================

Scieldas has a Docker image on `Docker Hub`_. You can either pull this image
directly::

    docker pull autophagy/scieldas

Or build the image yourself::

    docker build -t "autophagy/scieldas" .

To run the Docker image, you must first obtain the requisite API keys, which
you can then pass into the Docker container as an environment variable::

    docker run -d --name=scieldas-service -p 80:80 \
    --env TRAVIS_API_KEY=something autophagy/scieldas

In the container, gunicorn binds to port 80 - so map this port to whichever
port you want the service to be exposed on.

.. _Docker Hub: https://hub.docker.com/r/autophagy/scieldas/
