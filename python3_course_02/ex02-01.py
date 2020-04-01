# #输入和输出
#
#
#
# #在 Python 3 中，一般从终端获取用户的输入使用的是 input() 函数，
# # 括号中可以写入提示信息，用户的输入都是字符串类型，
# a =input ('please input your name:')
# print(a)
#
# b=input('please input a num:')
# print(type(b))
#
# # 用户输入的数字是一个字符串类型，通过 int() 函数可以将其转变为整数
# int(b)
# print(b)


#打印的内容中一小部分数据会经常变动，这个时候就可以使用到格式化输出。
# 格式化输出常用的有两种方式：
# 一种是 %+字母 的形式，
# 另一种是使用 format() 函数。


#%字母
print("%s is %d years old"%('Jack',8))
print("Apple's price is %.2f"%3.278)

#format() :
#在字符串中使用大括号 {} 表示一个数据，
# 大括号中的 0 表示 format() 函数中的第一个数据。
# 大括号中的 :.2f 表示四舍五入显示两位。

print("{} is {} years old".format('Jack',8))
print("Apple's price is {:.2f}".format(3.298))