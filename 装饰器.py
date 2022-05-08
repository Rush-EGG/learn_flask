import functools

# @app.route('xxx')  # endpoint默认是函数名，即login
# def login():
#     pass

'''

def auth(func):
    # 如果没有下面这行装饰器，那么login.__name__是inner
    # 因为相当于login被inner函数替换了
    # 但有了这行装饰器，login.__name__ = login
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@auth
def login():
    pass


@auth
def index():
    pass


print(login.__name__)
print(index.__name__)

'''


def auth0(func):
    print(0)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


def auth1(func):
    print(1)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@auth0
@auth1
def index():
    print('index')
