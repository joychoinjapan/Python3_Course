# 继承与方法重写#
# 继承分为两种：单继承和多继承。单继承是指子类只继承于一个父类，相应的多继承是指子类继承于多个父类。

# 将猫和狗都抽象为动物
class Animal(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self._age=age
    def make_sound(self):
        print(self.get_name() + ':wangwangwang')

    def get_age(self):
        return  self._age


class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ':NyaNay')


dog = Dog('wangwang',12)
cat = Cat('Nyanya')
cat.make_sound()
dog.make_sound()
print(dog.get_age())