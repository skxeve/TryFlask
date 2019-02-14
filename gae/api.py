from flask import Blueprint, current_app, jsonify, Flask

var_count = 999

api = Blueprint('api_v1', __name__)

@api.route('/hello')
def hello():
    current_app.logger.info("called hello method, name={}".format(__name__))
    return jsonify({
        "Message": "Hello flask jsonify",
        "Value": var_count,
    })


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(host='0.0.0.0', port=8080, debug=True)
