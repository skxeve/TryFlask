from flask import Flask, render_template, request, redirect, url_for
import numpy

app = Flask(__name__)

def get_random_message():
    messages = [
        "こんにちは。あなたの名前は？",
        "やあ！お名前は何ですか？",
        "What is your name?",
    ];
    return numpy.random.choice(messages)

@app.route('/')
def index():
    title = "***タイトル***"
    message = get_random_message()
    # index.htmlをレンダリング
    return render_template('index.html', message=message, title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title="ポストされたよ"
    if request.method == "POST":
        name = request.form['name']
        return render_template('index.html', name=name, title=title)
    else:
        # POSTメソッド以外なら一応ログ出ししてリダイレクトする
        app.logger.info("Invalid request method {}, Redirect for {}".format(request.method, url_for('index')))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
