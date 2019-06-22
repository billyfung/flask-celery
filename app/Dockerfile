FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install pipenv
ENV FLASK_ENV=production

RUN pipenv install --system --deploy
