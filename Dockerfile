FROM python:3.6-alpine

RUN mkdir -pv /app
ADD /scieldas /app
ADD requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
