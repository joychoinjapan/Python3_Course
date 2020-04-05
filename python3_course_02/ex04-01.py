#高阶函数
#高阶函数（Higher-order function），简言之就是可以接受函数作为参数的函数
# def f(func):
#     pass

#sorted 函数
l = ['Python', 'hello', 'linux', 'Git', 'Shiyanlou']
l_1=sorted(l)
print(l_1)

l=[1, 2, 3, -1, -2, -3, 0]
l_2=sorted(l)
print(l_2)

#abs 绝对值
print(abs(-99))
print(abs(0))

#sorted 的高阶用法举例
# abs 函数作为 key 参数的值，按照数字的绝对值进行排序
l = [1, 2, 3, -1, -2, -3, 0]
print(sorted(l,key=abs))

#思考题
#请使用 sorted 函数对该列表按球员名字进行排序：
pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]
print(sorted(pp,key=lambda x:x[0]))