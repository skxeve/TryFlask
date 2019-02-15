from flask import Flask
import logging
from top import top
from api import api

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.register_blueprint(top)
app.register_blueprint(api, url_prefix='/api/v1')

app.logger.info("main.py name={}".format(__name__))

var_count = 1


@app.route('/hello')
def hello():
    return 'Hello Flask37 GAE! var_count=' + str(var_count)


if __name__ == '__main__':
    var_count += 1
    app.run(host='0.0.0.0', port=8080, debug=True)
