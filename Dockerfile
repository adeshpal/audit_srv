# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update && apt install -y build-essential && apt install default-libmysqlclient-dev -y

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers=1", "--threads=3", "src.app", "--timeout", "600"]