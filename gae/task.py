from flask import Blueprint, current_app, jsonify, Flask, make_response
from google.cloud import tasks_v2beta3
import os

task = Blueprint('task', __name__)

project = os.getenv('GOOGLE_CLOUD_PROJECT', 'project_id')
queue = os.getenv('QUEUE_NAME', 'default')
location = os.getenv('QUEUE_LOCATION', 'us-central1')


@task.route('/short')
def short():
    sec = 3
    current_app.logger.info("called task short method, sec={}".format(sec))
    result = {
        "result": enqueue_sleep_task(sec),
        "sec": sec,
    }
    return make_response(jsonify(result))


@task.route('/long')
def long():
    sec = 180
    current_app.logger.info("called task long method, sec={}".format(sec))
    result = {
        "result": enqueue_sleep_task(sec),
        "sec": sec,
    }
    return make_response(jsonify(result))


@task.route('/toolong')
def too_long():
    # 60sec * 60min * 3hour
    sec = 60 * 60 * 3
    current_app.logger.info("called task too-long method, sec={}".format(sec))
    result = {
        "result": enqueue_sleep_task(sec),
        "sec": sec,
    }
    return make_response(jsonify(result))


@task.route('/specify/<int:sec>')
def specify(sec):
    current_app.logger.info("called task specify method, sec={}".format(sec))
    result = {
        "result": enqueue_sleep_task(sec),
        "sec": sec,
    }
    return make_response(jsonify(result))


def enqueue_sleep_task(sec):
    try:
        # taskqueue.add(url="/api/v1/sleep/{}".format(sec))
        client = tasks_v2beta3.CloudTasksClient()
        parent = client.queue_path(project, location, queue)
        current_app.logger.info("task parent={}".format(parent))
        item = {
            'app_engine_http_request': {  # Specify the type of request.
                'http_method': 'GET',
                'relative_uri': '/api/v1/sleep/{}'.format(sec),
            }
        }
        response = client.create_task(parent, item)

        current_app.logger.info(
            "task enqueue succeeded, name={} sec={}".format(response.name, sec)
        )
        return True
    except BaseException as e:
        current_app.logger.error(
            "Exception occurred {}: {}".format(type(e), e)
        )
        return False


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(task, url_prefix="/task/v1")
    app.run(host='0.0.0.0', port=8080, debug=True)
