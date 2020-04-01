#写入文件
#最常用的写入文件的方法是 write()，

#这样文件会被重写
filename=r"test.txt"
with open(filename,'w') as file:
    file.write('testline1')
    file.write('testline2')

with open(filename,'r') as file:
    print(file.readlines())

# 这样文件会在末尾被追加
with open(filename,'a') as file:
    file.write('testline3')
    file.write('testline4')