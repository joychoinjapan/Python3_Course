# 变量作用域

# 函数外使用global
# a=9
# def change():
#     global a
#     print(a)
#     a=100
# print("Before the function call ", a)
# print("inside change function", end=' ')
# change()
# print("After the function call ", a)

# 函数内使用global
def change():
    global a
    a = 90
    print(a)
a = 9
print("Before the function call ", a) #9
#程序中的 end=' ' 参数表示，print 打印后的结尾不用换行，而用空格。默认情况下 print 打印后会在结尾换行。
print("inside change function", end=' ')
change()#90
print("After the function call ", a)#90
