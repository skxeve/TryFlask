from flask import Blueprint, current_app

top = Blueprint('top', __name__)


@top.route('/')
def top_page():
    current_app.logger.info('info log')
    return 'TopPage!!'


@top.route('/hoge')
def hoge_page():
    current_app.logger.warning('debug called')
    return 'hoge'
