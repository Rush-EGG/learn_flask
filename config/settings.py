XX = 123

X1 = 234

# 正式数据库
DB_HOST = '192.168.16.88'

try:
    from .localsettings import *
except ImportError:
    pass


class BaseSettings(object):
    x = 123


class DevSettings(BaseSettings):
    HOST = '1.1.1.1'


class ProdSettings(BaseSettings):
    HOST = '1.1.1.2'
