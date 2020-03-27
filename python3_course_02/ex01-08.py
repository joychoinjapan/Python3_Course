#静态方法
#静态方法在运行时不需要实例的参与，它被放在类下面只是因为它和类有一点关系，但并不像类方法那样需要传递一个 cls 参数。

class Animal(object):
    owner = 'jack'
    def _init_(self,name):
        self._name = name

    @staticmethod
    def order_animal_food():
        print('ording.......')
        print('ok')

Animal.order_animal_food()