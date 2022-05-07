from flask import Flask

# 创建flask函数
app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello World'


@app.route('/login')
def index():
    return '登录页面'


if __name__ == '__main__':
    app.run()
