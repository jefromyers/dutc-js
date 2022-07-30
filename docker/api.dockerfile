FROM python:3.10.5-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY ./api/req.txt /api/req.txt

RUN pip install --no-cache-dir -r req.txt
