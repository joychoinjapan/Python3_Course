#函数的参数
#必选参数、默认参数、可变参数和关键字参数。

#1.必选参数 必须要按照顺序传参
#如果不按照定义顺序传参，就要使用参数名进行传参
# def connect(ipaddress, port):
#     print("IP: ", ipaddress)
#     print("Port: ", port)
#
# connect('192.168.1.1', 22)
# connect(22, '192.168.1.1')
# connect(port=22, ipaddress='192.168.1.1')


#2.函数的参数可以设定默认值，这种参数称为默认参数
#函数的参数可以设定默认值，这种参数称为默认参数。调用函数时，如果我们对默认参数没有赋值，则会自动赋其默认值。
# def connect(ipaddress,port=22):
#     print("IP:",ipaddress)
#     print("Port:",port)
# connect('192.168.1.1')

#顺序问题，默认参数后面不能再有必选参数，例如 f(a,b=90,c) 就是错误的
#默认参数的默认值必须设为不可变的数据类型（如字符串、元组、数字、布尔值、None 等）

#3.可变参数
#可变参数的定义格式是在参数名前面加上 * ，参数名可以自定义，通常写成 *args
#注意：在函数体内部使用该参数时，前面不要加 *
def connect(ipaddress, *ports):
    print("IP: ", ipaddress)
    print(ports)
    for port in ports:
        print("Port: ", port)
connect('192.168.1.1',22,23,24)
params=(25,39,44)
connect('192.168.1.1',*params)
#调用含可变参数的函数时，如果在可变参数的位置传入多个参数而不是元组，那么这些参数会自动生成一个元组传入函数。

