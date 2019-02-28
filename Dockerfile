FROM python:3.7-slim

RUN apt-get update \
 && mkdir -p /usr/share/man/man1 \
 && mkdir -p /usr/share/man/man7 \
 && apt-get -y install gcc libpq-dev python3-cairosvg wget curl python3-pil fontconfig make postgresql

RUN wget -O Inconsolata.ttf https://raw.github.com/google/fonts/master/ofl/inconsolata/Inconsolata-Regular.ttf \
 && mv Inconsolata.ttf /usr/share/fonts/truetype \
 && fc-cache -fv

RUN mkdir -pv /app/scieldas
ADD /scieldas /app/scieldas
ADD setup.py /app/setup.py
ADD Makefile /app/Makefile

EXPOSE 80

WORKDIR /app
RUN pip install --upgrade pip setuptools && make install
HEALTHCHECK CMD curl --fail http://localhost:80/_/health || exit 1
ADD README.md /app/README.md
ADD gunicorn_config.py /app/gunicorn_config.py
ADD logging.conf /app/logging.conf

ARG COMMIT=""
LABEL commit=${COMMIT}
ENV COMMIT_SHA=${COMMIT}

ENTRYPOINT ["make"]
CMD ["production"]
