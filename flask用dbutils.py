from flask import Flask
import sqlhelper
from sqlhelper2 import db

app = Flask(__name__)


@app.route('/login')
def login():
    result = sqlhelper.fetchone('select * from student where Sdept=%s', 'CS')
    print(result)
    return 'login'


@app.route('/index')
def index():
    result = sqlhelper.fetchall('select * from student where Sdept=%s', 'CS')
    print(result)
    return 'xxx'


@app.route('/order')
def order():
    # print(db)
    conn, cursor = db.open()
    # 自己做操作
    db.close(conn, cursor)

    return 'xxx'


if __name__ == '__main__':
    app.run()
