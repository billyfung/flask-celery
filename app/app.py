from flask import Flask, url_for
from redis import Redis
from worker import celery
from decimal import Decimal
import celery.states as states


SAMPLE_DATA = {
    'A': 1,
    'B': 2,
    'C': 4
}

# initialise the app
app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'This has been viewed %s time(s).' % redis.get('hits')

@app.route('/process')
def process_data():
    task = celery.send_task('tasks.process', args=[SAMPLE_DATA], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)