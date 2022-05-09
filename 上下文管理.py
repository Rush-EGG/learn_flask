# class Foo(object):
#     def __enter__(self):
#         return "我进来了"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return "我出来了"
#
#
# # 实例化一个Foo对象
# obj = Foo()
#
# # 通过with会自动执行该对象中的enter方法，再执行exit方法
# with obj as f:
#     print(f)

class Foo(object):
    def do_something(self):
        print("我是猪")

    def close(self):
        pass


class Context:
    def __enter__(self):
        self.data = Foo()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("你才是猪")
        self.data.close()


with Context() as ctx:
    # ctx是通过Context的__enter__方法返回得到的对象，所以有do_something()方法
    ctx.do_something()
