FROM python:3.9.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev bash

RUN pip install --upgrade pip
COPY ./bank_django_nuxt3_api/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app/bank_django_nuxt3_api

EXPOSE 8000

COPY . .

ENTRYPOINT ["./.docker/entrypoint.sh"]