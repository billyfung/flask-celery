FROM python:3.6-alpine

ENV C_FORCE_ROOT true
RUN apk add build-base
RUN apk add postgresql-dev

COPY . /queue
WORKDIR /queue

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks worker --loglevel=info