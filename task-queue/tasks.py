import os
import time
from celery import Celery


CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL',
    'redis://localhost:6379'
)
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 
    'redis://localhost:6379'
)

celery = Celery(
            'tasks', 
            broker=CELERY_BROKER_URL, 
            backend=CELERY_RESULT_BACKEND
)


@celery.task(name='tasks.process')
def process(input_data):
    time.sleep(5)
    output_data = input_data
    return output_data