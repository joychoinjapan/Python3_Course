#__call__通过calllable()来判断一个对象是否为可调用对象

class Animal(object):
    def __call__(self):
        print('call')

dog = Animal()
print(callable(dog))


#下面这个例子可以记录 num_counter 函数被调用的次数：
class Counter(object):
    def __init__(self,func):
        self.func=func
        self.count=0
    def __call__(self, *args, **kwargs):
        self.count +=1
        return self.func(*args, **kwargs)

#类作为一个装饰器来使用
@Counter
def num_counter():
    pass

for i in range(20):
    num_counter()

print(num_counter.count)