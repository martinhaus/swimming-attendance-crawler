FROM python:3.7

LABEL maintainer "Martin Hauskrecht <martin@hauskrecht.sk>"

RUN apt-get update

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0