FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
COPY . /api

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt
