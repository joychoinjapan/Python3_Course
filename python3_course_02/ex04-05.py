#偏函数

from functools import partial
def cal_power(i,m=2):
    return i**m
#partial 函数接受两个参数，
# 第一个参数为原函数名，
# 第二个参数为原函数中的默认参数
# partial 函数的返回值就是一个我们需要的新函数。
cal_power4 = partial(cal_power,m=4)
print(cal_power4(3))

##切片
#切片用于获取一个序列（列表或元组）或者字符串的一部分，返回一个新的序列或者字符串，
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:3])
print(letters[1:-4])

#省略 start 则默认 start 为 0，省略 end 则默认截取到最后：
print(letters[:4])
print(letters[4:])

#可以利用切片返回新列表的特性来复制一个列表：
copy =letters[:]
print(copy)


##列表解析（list comprehension）
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 获取 numbers 中的所有偶数
print([x for x in numbers if x % 2 == 0])
# 对 numbers 的每个数求平方
print([x * x for x in numbers])

##字典解析（dict comprehension）
d = {'a': 1, 'b': 2, 'c': 3}
#items() 获取字典的 key 和 value 值
print({k:v*v for k,v in d.items()})

##元组拆包
#允许等号左边的变量依次被元组内的元素赋值
t = ('hello', 'shiyanlou')
a,b=t
print(a)
print(b)

#元组拆包还有一个比较特殊的格式，就是用 * 达到拆包的作用
t =('Tom',11)

print('I\'m {}, I\'m {} years old.'.format(*t))



