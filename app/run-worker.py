import os
import redis
from rq import Worker, Connection, Queue


listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL')
if not redis_url:
    raise RuntimeError('Missing Redis Server URL.')

redis_connection = redis.from_url(redis_url)


if __name__ == '__main__':
    with Connection(redis_connection):
        worker = Worker(map(Queue, listen))
        worker.work()