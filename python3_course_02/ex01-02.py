#封装
class Dog(object):
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name=value
    def bark(self):
        print(self.get_name()+':wangwang')

class Cat(object):
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name.lower().capitalize()
    def set_name(self,value):
        self._name=value
    def mew(self):
        print(self.get_name()+':miu miu miu')

dog=Dog('wangwang')
cat=Cat('nyanya')
dog.bark()
cat.mew()
print(cat.get_name())