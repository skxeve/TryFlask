from flask import Flask

app = Flask(__name__)

var_count = 1

@app.route('/')
def hello():
    return 'Hello Flask37 GAE! var_count=' + str(var_count)

if __name__ == '__main__':
    var_count += 1
    app.run(host='0.0.0.0', port=8080, debug=True)
