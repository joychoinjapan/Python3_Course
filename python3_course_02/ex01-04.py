#多继承
#多继承是指一个子类继承了多个父类，因此这个子类也相应地拥有了所有父类的属性，可以调用所有父类中的方法。

class A:
    def __init__(self):
        self.name = 'xiaoming'
    def testA(self):
        print('----testA----')

class B:
    def __init__(self):
        self.age=11
    def testB(self):
        print('----testB----')

class Person(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def testPerson(self):
        print('----testPerson----')

person = Person()
print(person.name)
print(person.age)
person.testA()
person.testB()
person.testPerson()
