FROM python:3.6-slim

RUN apt-get update && apt-get -y install libmagickwand-dev wget curl

RUN wget -O Inconsolata.ttf https://raw.github.com/google/fonts/master/ofl/inconsolata/Inconsolata-Regular.ttf
RUN mv Inconsolata.ttf /usr/share/fonts/truetype
RUN ls /usr/share/fonts/truetype
RUN fc-cache -fv

RUN mkdir -pv /app/scieldas
ADD /scieldas /app/scieldas
ADD setup.py /app/setup.py
ADD README.rst /app/README.rst
ADD gunicorn_config.py /app/gunicorn_config.py
ADD logging.conf /app/logging.conf

EXPOSE 80

WORKDIR /app
RUN pip install e .
HEALTHCHECK CMD curl --fail http://localhost:80/_/health || exit 1
ENTRYPOINT ["gunicorn"]
CMD ["--config", "/app/gunicorn_config.py", "--log-config", "/app/logging.conf", "scieldas"]
