# dict (字典)
# 字典中的每一个元素都是一个key 和 一个 value 的组合，
# key 值在字典中必须是唯一的，因此可以很方便的从字典中使用 key 获得其对应的 value 的值。

coursedict = {1: 'linux', 2: 'vim', 'a': 'jojo', 'b': 'cho'}
print(coursedict)
print(coursedict.get(2))
print(coursedict.get(9))

# 创建字典 dict()
dict_from_tuple = dict(((1, 'Linux'), (2, 'Vim')))
print(dict_from_tuple)

# 取值
print(dict_from_tuple.get(1))

# 赋值
coursedict = dict()
coursedict[5] = 'Bash'
coursedict[6] = 'Python'
coursedict[7] = 'Java'
print(coursedict)

# 删除
del coursedict[5]
print(coursedict)

# 遍历
for key, value in coursedict.items():
    print(key, value)

#只获取字典中的key 和value 列表
print(coursedict.keys())
print(coursedict.values())

#删除指定的key：value php()
print(coursedict.pop(7))
print(coursedict)