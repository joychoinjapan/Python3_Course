#创建类和实例对象

class Dog:
    pass
dog=Dog()# 创建类的实例对象
dog.name='gigi'# 给实例对象绑定 name 属性
print(dog.name)# 访问 dog 实例对象的 name 属性

#对实例进行初始化设置
# 设置一些默认的值，通过这个类创建的实例对象将默认拥有这些值（属性）
class Dog_2:
    def __init__(self):
        self.name = "gigi2"
dog = Dog_2()
print(dog.name)

#从外面传递数据给类，用来绑定数据到对应的属性上
class Dog_3:
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog=Dog_3('gigi3',2)
print(dog)
print(dog.name)
print(dog.age)

#使用类的另一个内置方法 __repr__ 来格式化实例的打印格式
class Dog_4:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return 'Dog:{}'.format(self.name)
dog=Dog_4('gigi4',10)
print(dog)
print(dog.name)
