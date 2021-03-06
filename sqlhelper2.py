import pymysql
from DBUtils.PooledDB import PooledDB


class SqlHelper(object):
    # pass
    def __init__(self):
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的链接，0表示不创建
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always

            host='127.0.0.1',
            port=3306,
            user='root',
            password='13004276060',
            database='sct',
            charset='utf8'
        )

    def open(self):
        conn = self.POOL.connection()
        cursor = conn.cursor()

        return conn, cursor

    def close(self, cursor, conn):
        cursor.close()
        conn.close()

    def fetchone(self, sql, *args):
        """ 获取单条数据 """
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.close(cursor, conn)

        return result

    def fetchall(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(cursor, conn)

        return result

    def __enter__(self):
        # 只要cursor所以取数组下标为1的，即第二个元素
        return self.open()[1]

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        # self.cursor.close()


db = SqlHelper()
