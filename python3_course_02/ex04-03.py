#map/reduce
from functools import reduce
#map(a,b)
# a 是函数，用来处理 b 参数
# b 是可迭代对象
b = [1, -2, 3, -4, -5, 6, 7, 8, -9]
#我们要得到它的每个元素的平方的值，并生成新的列表。
# 先写 a 函数，用来处理每个元素：

def a(i):
    return i**2

print(list(map(a,b)))


#reduce
#reduce 的 a 函数对 b 序列做积累处理
def a(x,y):
    return x+y
#需要注意的一点：reduce 在 python2 中同 map 函数一样可以直接使用，在 python3 中需要从 functools 库中引入：
print(reduce(a,b))


#思考题:使用 map 方法得到所有球员名字的全小写列表：
pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

def changeName(name):
    return name[0].lower()


print(list(map(changeName,pp)))