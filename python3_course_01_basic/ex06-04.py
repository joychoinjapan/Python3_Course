def connect (ipaddress,ports):
    ipaddress = '10.10.10.1'
    print("IP:",ipaddress)
    print("Ports",ports)
    ports.append(8080)

if __name__=="__main__":
    ipaddress='192.168.1.1'
    ports= [22,23,24]
    print("Before connect:")
    print("IP:",ipaddress)
    print("Ports:",ports)
    print("In connect:")
    connect(ipaddress,ports)
    print("After connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)

#Python 中的对象有不可变对象:数值、字符串、元组等
#可变对象:指的是列表、字典等。
#如果是不可变对象作为参数，函数中对该参数的修改只能用等号赋值，实际上是创建了一个新的局部变量。如果是可变对象作为参数，函数中的修改会保留。