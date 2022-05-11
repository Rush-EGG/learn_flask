from flask import Flask, render_template
from werkzeug.routing import BaseConverter

app = Flask(__name__, )


# 正则表达式转换方法
class RegConverter(BaseConverter):
    def __init__(self, map, regex):
        super.__init__(map)
        self.regex = regex


app.url_map.converters['regex'] = RegConverter


@app.route('/index/<name>')
def index(name):
    print(type(name))
    return render_template('index.html')


@app.route('/login/<regex("\d+"):x1>')
def index(x1):
    print(x1, type(x1))
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
