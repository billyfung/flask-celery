import os
import time
from celery import Celery
import psycopg2
from random import randint


CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL',
    'redis://redis:6379'
)
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 
    'redis://redis:6379'
)

celery = Celery(
            'tasks', 
            broker=CELERY_BROKER_URL, 
            backend=CELERY_RESULT_BACKEND
)

DB_CONN = "dbname=testdb user=testuser password=password host=db"
INSERT_SQL = """
    insert into test_table (col_a, col_b, test_value) 
    values (%s, %s)
"""

@celery.task(name='tasks.process', ignore_result=True)
def process(input_data):
    time.sleep(1)
    A = int(input_data['A'])
    B = int(input_data['B'])
    C = int(input_data['C'])
    with psycopg2.connect(DB_CONN) as conn:
        with conn.cursor() as c:
            c.execute(
                INSERT_SQL, 
                (
                    A*randint(1,100), 
                    B*randint(1,100), 
                    C*randint(1,30))
            )