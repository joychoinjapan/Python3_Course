# 在代码中需要满足以下要求：
#
# 使用 input() 获取用户输入的三个整数值
# 对这三个整数值使用加法进行求和并打印输出
# 打印时需要使用 format() 函数


first=input('Please enter the first num:')

second=input('Please enter the second num:')

third=input('Please enter the third num:')

sum=int(first)+int(second)+int(third)

print("a is {}, b is {}, c is {}, a+b+c ={}".format(first,second,third,sum))
