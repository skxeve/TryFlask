from flask import Blueprint, current_app, jsonify, Flask, make_response
from time import sleep
import os

var_count = 999

api = Blueprint('api_v1', __name__)


@api.route('/hello')
def hello():
    current_app.logger.info("called hello method, name={}".format(__name__))
    return jsonify({
        "Message": "Hello flask jsonify",
        "Value": var_count,
    })


@api.route('/sleep/<int:sec>')
def sleep_logging(sec):
    current_app.logger.warning("api sleep_logging called, sec={}".format(sec))
    if sec > 120:
        per = 10
    elif sec > 50:
        per = 5
    else:
        per = 1
    for i in range(sec):
        sleep(1)
        if i % per == per - 1:
            current_app.logger.info("sleeping {}/{} sec.".format(i + 1, sec))
    result = {
        "result": True,
        "sec": sec,
    }
    current_app.logger.info("api sleep_logging finished, result={}".format(result))
    return make_response(jsonify(result))


@api.route('/env/list')
def env_list():
    data = {}
    count = 0
    for key, value in os.environ.items():
        data[key] = value
        count += 1
    result = {
        "data": data,
        "count": count,
    }
    return make_response(jsonify(result))


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api/v1")
    app.run(host='0.0.0.0', port=8080, debug=True)
