#filter 也是一个 Python 内建的高阶函数，它的作用是对序列进行过滤。
# 函数的高阶用法，会接受一个函数作为参数，filter 也是如此

#格式：filter(a,b)
# a 为函数，b 为被处理的数据列表
# a 会对 b 中的每个元素进行判断，结果为真则保留，否则舍弃
#函数 isinstance ，它接受两个参数，
# 作用是判断数据的数据类型

##第一种写法
b = [9, 'Python', True, 3.14, 2019, -4, abs]
def a(i):
    if isinstance(i,int):
        return True
    else:
        return False

print(list(filter(a,b)))

#思考题
#仍然对上一个思考题中的 pp 列表进行处理，
# 使用 filter 函数对其进行过滤，得到能力值为 96+（含 96）的球员的数据：
pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

#定义函数
def select_score(list):
    if list[1]>=96:
        return True
    else:
        return False
print(list(filter(select_score,pp)))

#用匿名函数
print(list(filter(lambda array:array[1]>=96,pp)))