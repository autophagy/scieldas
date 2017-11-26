FROM python:3.6-alpine

RUN mkdir -pv /app/scieldas
ADD /scieldas /app/scieldas
ADD setup.py /app/setup.py
ADD README.rst /app/README.rst

WORKDIR /app
RUN pip install e .
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:8080", "scieldas"]
