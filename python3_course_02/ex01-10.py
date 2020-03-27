#在 Python 中有一些特殊的方法，它们是 Python 内置的方法，
#通常以双下划线来命名，比如 __init__、__repr__ 等等，
#在类中使用它们时往往较少的代码就可以发挥很大的作用，
#提高开发效率，因此在 Python 中称这些方法为“魔法方法”。

# __init__:
# 新建实例对象的时候给对象绑定属性
# 第一个参数为self，不需要返回值
#
# __new__:
# 在实例对象被创建之前调用的，主要用于创建实例对象并返回实例对象，
# 它的第一个参数为 cls ，它只会取 cls 参数，其余参数都传给了 __init__ 方法，
# 必须要有返回值可以是 super().__new__(cls) 或是 object.__new__(cls)

#__del__:
# 在执行 del 实例对象 的时候真正调用的是类中的 __del__ 方法，
# 它定义了当对象被销毁时需要执行的行为。

class Animal(object):
    def __new__(cls,name):
        print("__new__")
        return super(Animal,cls).__new__(cls)
    def __init__(self,name):
        print("__init__")
        self.name=name
    def __del__(self):
        print("__del__")
cat = Animal('tom')
print(cat.name)
del cat
