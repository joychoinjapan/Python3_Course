#读取文件
#read()可以一次性读取整个文件的内容到字符串

filename=r"test.txt"
file = open(filename)
print(file.read())
file.close()

print('-----------------------')
with open(filename) as file:
    print(file.read())#项目开发中，我们需要谨慎使用 read() 读取整个文件
file.close()

print('-----------------------')
#逐行处理
file=open(filename)
print(file.readline())
print(file.readline())
file.close()
print('-----------------------')
#readlines() 可以读取所有行，并形成列表
file=open(filename)
print(file.readlines())
file.close
print('-----------------------')
#for 循环遍历文件对象来读取文件中的每一行：
with open(filename) as file:
    for line in file:
        print(line,end='')
file.close()