from math import pi
result=5*5*pi
print(result)

#None
# type(None)
# <class 'NoneType'>
# type('')
# <class 'str'>
# type(0)
# <class 'int'>

#Bool
# bool(None)
# False
# bool(1)
# True
# bool(0)
# False
# bool(False)
# False
# bool(True)
# True

#保留字与标识符
#保留字，又称为关键字，每种语言都有自己的一套预先保留的特殊标识符，Python 也不例外，它自带的 keyword 模块可以查看全部关键字。在 Python3 交互式命令行中执行如下命令，引入 keyword 模块就可以查看到 Python 中的关键字：

# >>> import keyword
# >>> keyword.kwlist

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#内置函数(方法)
#函数在一些情况下又被称作方法，例如在类中。Python 内置了大量很好用的函数，这些函数分别支持一些基本的功能。可以通过在 Python 交互式解释器中执行 help() 来获取这些内置函数的帮助，例如我们希望查看 len() 函数的作用：

# >>> help(len)

#变量
# 编程语言中为了能够更好的处理数据，都需要使用一些变量。变量基本上就是代表（或是引用某值的名字）。Python 语言的变量可以是各种不同的数据类型，使用变量的时候不需要声明，Python 解释器会自动判断数据类型。使用 type(变量名)可以查看该变量的类型。

a=3
print(type(a))#<class 'int'>

b="shiyanlou"
print(type(b))#<class 'str'>

a=3.4
print(type(a))#<class 'float'>


