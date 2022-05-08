from flask import Flask
import functools

# 创建flask函数
app = Flask(__name__)


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@app.route('/index')
@auth
def index():
    return 'Hello World'


@app.route('/login')
@auth
def login():
    return '登录页面'


if __name__ == '__main__':
    app.run()
