# Flaskクラスをインポートしている。
# FlaskインスタンスはWSGI(WebServerGatewayInterface)アプリケーション
from flask import Flask
# インスタンス生成
app = Flask(__name__)

# routeデコレータを使用し、ルーティングをFlaskに登録
@app.route('/')
def hello_world():
    return "Hello World!"

# URLで変数を受け取る
@app.route('/user/<username>')
def show_user_profile(username):
    return "Username is " + username

# URLで受け取る変数に型を指定する。型と違う場合404になる
@app.route('/post/seisu/<int:id>')
def show_id(id):
    return "ID is " + str(id)

@app.route('/post/shosu/<float:per>')
def show_per(per):
    return "percent is " + str(per)



# スクリプトがPythonで直接実行された時にだけ実行されることを保証する
# モジュールとしてインポートされた時には走らない
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
