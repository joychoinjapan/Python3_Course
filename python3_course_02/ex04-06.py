#迭代器
#可迭代对象都可以通过 iter 函数去获取它的迭代器，
# 比如letters 是一个可迭代对象，那么这样去迭代它：
letters = ['a', 'b', 'c']
it = iter(letters)
print(next(it))
print(next(it))
print(next(it))