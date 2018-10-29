FROM python:3.6.4-alpine3.7

RUN apk add --no-cache \
    build-base cairo-dev cairo cairo-tools wget curl \
    # pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN mkdir -pv /usr/share/fonts/truetype
RUN wget -O /usr/share/fonts/truetype/Inconsolata.ttf https://raw.github.com/google/fonts/master/ofl/inconsolata/Inconsolata-Regular.ttf && fc-cache -fv

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
