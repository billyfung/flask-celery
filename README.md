# flask-celery
Flask with celery task queue that does long processing job in the background
- use whatever external functions you'd like outside of app
- look into how to tie into using app models if needed

# setup
Using docker for everything

`docker-compose up`
will spin up redis and flask app container
http://localhost:5000/ contains the web app

# task queue
Celery with redis broker to do async processing
