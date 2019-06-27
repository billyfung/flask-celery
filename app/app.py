from flask import Flask, url_for, jsonify
from redis import Redis
from rq import Queue

from tasks import process_task

SAMPLE_DATA = {
    'uuid1': {
        1: 1.2,
        2: 1.5,
        3: 0.3,
        4: 0.1
    },
    'uuid2': {
        1: 0.2,
        2: 0.5,
        3: 1.3,
        4: 1.1
    }
}

# initialise the app
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
q = Queue(connection=redis)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This has been viewed %s time(s).' % redis.get('hits')

@app.route('/process')
def process_data():
    job = q.enqueue(process_task, SAMPLE_DATA)
    response = f"<a href='{url_for('check_task', task_id=job.get_id(), external=True)}'>check status of {job.get_id()} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    task = q.fetch_job(task_id)
    if task.get_status() == 'finished':
        response_object = {
            'status': 'success',
            'data': {
                'task_id': task.get_id(),
                'task_status': task.get_status(),
                'task_result': task.result,
            }
        }
    elif task.get_status() == 'started':
        response_object = {'status': 'working on it'}
    else:
        response_object = {'status': 'error'}
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)