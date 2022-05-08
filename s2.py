import functools

from flask import Flask, render_template, jsonify, request, redirect, url_for, session

app = Flask(__name__)

# 自定义一个secret_key，可以随便写，如果不写将不能用session
app.secret_key = 'woshizhuniyeshizhuma'

DATA_DICT = {
    1: {'name': "卢小喷", 'age': 8},
    2: {'name': "root", 'age': 88},
    3: {'name': "卢大喷", 'age': 1},
    4: {'name': "卢小添", 'age': 22},
}


# 用装饰器来验证用户登录
def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # 检查用户是否已登录
        log = session.get('xxx')
        if not log:
            return redirect(url_for('login'))

        return func(*args, **kwargs)

    return inner


# 在路由中添加method参数才可以让该url支持get和post
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
        # return '登录'  # 类似于HttpResponse
        # return render_template('login.html')  # 类似于render
        # return jsonify({'code': 1000, 'data': [1, 2, 3]})  # 类似于JsonResponse

    # print(request.form)
    user = request.form.get('user')
    pwd = request.form.get('pwd')

    if user == 'root' and pwd == '123':
        session['xxx'] = 'root'
        return redirect('/index')
    error = "用户名或密码错误"
    return render_template('login.html', error=error)


# 用endpoint可以给路由起别名
@app.route('/index', endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)


@app.route('/edit', methods=['GET', 'POST'])
@auth
def edit():
    nid = request.args.get('nid')
    # print(nid, type(nid))  # type(nid) = str
    nid = int(nid)

    if request.method == 'GET':
        info = DATA_DICT[nid]

        return render_template('edit.html', info=info)

    user = request.form.get('user')
    age = request.form.get('age')

    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age

    # 通过/index的别名'idx'去redirect
    return redirect(url_for('idx'))


@app.route('/delete/<int:nid>')
@auth
def delete(nid):
    # nid = request.args.get('nid')
    # print(nid)
    del DATA_DICT[nid]

    # return "删除" + nid
    # return redirect('/index')
    # 通过/index的别名'idx'去redirect
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run()
