# 类属性和类方法

# 类属性是类对象的属性，通过类对象定义的实例对象都可以拥有这个属性，但是在类外，只有公有的类属性才可以被直接访问。
class Animal(object):
    owner = 'jack'

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.owner

    @classmethod
    def set_owner(cls, name):
        cls.owner = name


animal = Animal('Jack')
print(animal.get_owner())
animal.set_owner('Rose')
print(animal.get_owner())
