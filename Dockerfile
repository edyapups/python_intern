FROM python:3.8-slim

COPY app /app
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

env PORT 8080
#CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
CMD gunicorn app.main:app --host 0.0.0.0 --port $PORT -w 4 -k uvicorn.workers.UvicornWorker
