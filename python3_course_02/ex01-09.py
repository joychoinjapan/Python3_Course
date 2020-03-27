#@property 装饰器可以将一个方法变成一个属性来使用，通过 @property 装饰器可以获得和修改对象的某一个属性。

#只有 @property 表示只读
#同时有 @property 和 @*.setter 表示可读可写
#同时有 @property、@*.setter、和 @*.deleter 表示可读可写可删除
#@property 必须定义在 @*.setter 的前面
#类必须继承 object 父类，否则 @property 不会生效


class Animal(object):
    def __init__(self):
        self.__age=3
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self.__age=value
        else:
            raise ValueError
    @age.deleter
    def age(self):
        print('delete age')
        del self.__age

cat = Animal() #创建实例
print(cat.age)
#cat.age='kdfdasf' #设置为字符串，报错
del cat.age
print(cat.age)