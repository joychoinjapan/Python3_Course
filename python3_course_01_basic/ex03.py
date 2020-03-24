#Python3 中的字符串可以使用双引号或单引号标示，如果字符串中出现引号，则可以使用 \ 来去除引号标示字符串的特殊作用。
str1="hello"#hello
str2='shiyanlou'#shiyanlou
str3='hello,\'shiyanlou\''#hello,'shiyanlou'
str4="hello,'shiyanlou'"#hello,'shiyanlou'
str5='hello,"shiyanlou"'#hello,"shiyanlou"

print(str5)

#字符索引
string='hello_shiyanlou'
print(string[0])
print(string[1])
print(string[2])
print(string[-1])
print(string[-2])

#切片即获取字符串的片段，格式为 [头索引:尾索引:步长]。索引又称作下标。
print(string[0:5])
print(string[:5])
print(string[6:15])
print(string[3:11:2])#取下标为 3 至 10 的字符，步长为 2 即每两个取第一个
#l_hy
print(string[::3]) #取下标为 3 至 10 的字符，步长为 2 即每两个取第一个
print(string[::-1])#这是一种特殊写法，步长为 -1 ，即反向取全部字符，也就是倒序排列

#字符串的常用属性和方法
#count() 获取字符串中某个字符的数量
print(string.count('l'))

#strip()
# 默认情况下会删除字符串首尾的空格及换行等空白符。如果strip()函数中使用参数则会删除这些参数中的字符（仅限于出现在字符串首尾的情况），例如 str1.strip('ab') 则只会删除 str1 字符串中头尾部的 a 和 b 字符。
#split()
# 默认情况下会删除字符串首尾的空格及换行等空白符。如果strip()函数中使用参数则会删除这些参数中的字符（仅限于出现在字符串首尾的情况），例如 str1.strip('ab') 则只会删除 str1 字符串中头尾部的 a 和 b 字符。

str1=' shiyanlou '
print(str1.strip())
str1='akkkkffab'
print(str1.strip('afb'))#kkkk
str3='hello shiyanlou'
list1=str3.split()
print(list1)
str4='hello:shiyanlou'
list2=str4.split(':')
print(list2)
str5='apple,orange,banana'
list3=str5.split(',')
print(list3)

#upper 和 lower
#前者将字符串中每个英文字母变成大写，后者将每个英文字母变成小写：
string='louplus_PYTHON'
print(string.upper())
print(string.lower())

#len()
#该方法等同于 Python3 中的内置函数 len()，可以获得字符串包括的字符数量：
print('louplus_python'.__len__())

#format 格式化字符串
#Python2.6 开始，新增了一种格式化字符串的函数 str.format()，
#它增强了字符串格式化的功能。format 是用法简单、使用频率极高的字符串方法。下面举例说明常用格式：

# 规定每个位置传入的参数
str='{1},{0},{1}'.format('hello','shiyanlou')
print(str)

#格式化 float 类型参数为字符串，并规定小数位数
str='圆周率：{:.2f}'.format(3.1415926)
print(str)

#通过字典设置参数，即带参数名的参数
str='网站：{name},地址：{url}'.format(name='shiyanlou',url='通过字典设置参数，即带参数名的参数')
print(str)

#成员运算符
# in not in
# 如果在指定的序列中找到值返回 True，否则返回 False
# 如果在指定的序列中没有找到值返回 True，否则返回 False
print('a' in ['a','b','c'])