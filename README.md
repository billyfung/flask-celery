# flask-celery
Flask with celery task queue that does long processing job in the background
- use whatever external functions you'd like outside of app
- look into how to tie into using app models if needed

The folder task-queue contains the local for whatever task is needed. The ideal is that if it's possible, remove the logic away from the app, then within the app we can return whatever is tied to each model. 

# setup
Using docker for everything

`docker-compose up`
Will spin up redis, flask app, worker and monitor containers
http://localhost:5000/ contains the web app

# task queue
Celery with redis broker to do async processing

to scale workers up
```
docker-compose up -d --scale worker=5 --no-recreate
```
