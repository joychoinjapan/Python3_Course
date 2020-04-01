#文件的打开和关闭
#open() 函数需要两个参数，
# 第一个参数是文件路径或文件名，
# 第二个是文件的打开模式。"r w a b"

with open('/etc/protocols') as file:
    count = 0
    for line in file:
        count+=1
    print(count)
    file.close()

