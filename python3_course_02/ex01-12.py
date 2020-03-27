#__getattribute__  __getattr__

class Animal(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def __getattribute__(self,attr):
        print('调用 self.__getattribute__ 方法，访问 {} 属性'.format(attr))
        if attr in ('name','gender'):
            # 如果 object.__getattribute__ 可以获取属性值，即返回属性值，否则自动调用 object.__getattr__ 方法
            return object.__getattribute__(self,attr)
        else:
            print('交给 object.__getattr__ 处理...')
            # 如果 Animal 类中有 __getattr__ 方法的话，object.__getattr__ 方法会自动调用 Animal 的同名方法
            return object.__getattr__(self,attr)
    def __getattr__(self,attr):
        print('调用了 self.__getattr__ 方法，访问 {} 属性'.format(attr))
        if attr == 'age':
            return 3
        else:
            return '未找到该属性'
