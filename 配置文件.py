from flask import Flask, render_template

app = Flask(__name__)

# 加载配置文件
app.config.from_object('config.settings')
app.config.from_object('config.settings.DevSettings')
app.config.from_object('config.settings.ProdSettings')

print(app.config['DB_HOST'])


@app.route('/index')
def index():
    return render_template('index_new.html')


if __name__ == '__main__':
    app.run()
