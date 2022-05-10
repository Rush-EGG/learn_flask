from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/index')
def index():
    return render_template('index_new.html')


if __name__ == '__main__':
    app.run()
