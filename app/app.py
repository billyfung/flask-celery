from flask import Flask
from redis import Redis
from celery import Celery
from decimal import Decimal


SAMPLE_DATA = {
    'uuid1': {
        1: Decimal(1.2),
        2: Decimal(1.5),
        3: Decimal(0.3),
        4: Decimal(0.1)
    },
    'uuid2': {
        1: Decimal(0.2),
        2: Decimal(0.5),
        3: Decimal(1.3),
        4: Decimal(1.1)
    }
}

# initialise the app
# TODO: use envars for hosts
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
celery = Celery(broker='redis://localhost:6379/0')


@app.route('/')
def hello():
    redis.incr('hits')
    return 'This has been viewed %s time(s).' % redis.get('hits')

@celery.task(name='calc.processing')
def processing():
    from external_lib import process_data
    output = process_data(SAMPLE_DATA)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)