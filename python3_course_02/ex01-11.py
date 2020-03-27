#__slots__
#如果需要闲置绑定属性类别，可以使用__slots__变量
#可以绑定的属性值以元组的形式赋予给它。
class Animal(object):
    __slots__=('name','age')

dog = Animal()
dog.name='wangcai'
dog.age=2
dog.gender='male'#无法定义性别，会报错