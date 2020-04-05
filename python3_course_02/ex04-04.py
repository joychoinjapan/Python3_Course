#匿名函数
#匿名函数，顾名思义，这类函数没有函数名，
# 这个特点的好处是避免自定义变量名冲突、减少代码量、使代码结构更加紧凑。
# 缺点是不可重复使用。

double=lambda x:x*2
print(double(5))

#例子中使用 lambda 定义了一个匿名函数。 lambda 返回值时不需要 return
b = [1, -2, 3, -4, -5, 6, 7, 8, -9]
#对 b 列表中的元素进行求平方，然后得到新的列表
print(list(map(lambda i:i**2,b)))


#用 lambda 和 map 获取 pp 列表中球员的名字的全大写列表并使用 sorted 函数进行降序排序（一行代码实现）
pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]
print(sorted(list(map(lambda name:name[0].upper(),pp)),reverse=True))