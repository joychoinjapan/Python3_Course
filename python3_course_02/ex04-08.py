#装饰器#
#装饰器(Decorators)是 Python 的一个重要部分。简单地说：他们是修改其他函数的功能的函数。
# 他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。大多数初学者不知道在哪儿使用它们，所以我将要分享下，哪些区域里装饰器可以让你的代码更简洁。

def hi(name="yasoob"):
    return "hi"+name

print(hi())

#将一个函数赋值给一个变量
greet = hi
print(greet())

del hi
# print(hi())

#这个依然能够执行哦
print(greet())

print("---------------------------------------------------")
#在 Python 中我们可以在一个函数中定义另一个函数

def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
print("---------------------------------------------------")
# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：
#greet()
# outputs: NameError: name 'greet' is not defined

#从函数中返回函数

#其实并不需要在一个函数里去执行另一个函数
# 我们也可以将其作为输出返回出来：
def hi2(name="yasoob"):
    #把一对小括号放在后面，这个函数就会执行；
    # 然而如果你不放括号在它后面， 那它可以被到处传递，并且可以赋值给别的变量而不去执行它。
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a=hi2("yahoooda")
print(a)
#这种情况下a（）内不能赋值了
print(a())


#将函数作为参数传给另一个函数
def hi3():
    return "hi yasoob!"
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi3)
print("---------------------------------------------------")
#你的第一个装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
print("---------------------------------------------------")
a_function_requiring_decoration=a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

print("---------------------------------------------------")

#改写成@的方式
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")
a_function_requiring_decoration()

#用@的方式和下述写法是一样的
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)