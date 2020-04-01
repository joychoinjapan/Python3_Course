import os
#实现文件内容统计程序
#这个程序接受用户输入的字符串作为将要读取的文件的文件名，
# 并且在屏幕上打印文件行数和文件内容，程序写入

current_name=os.path.abspath(__file__)
fater_dir=os.path.abspath(os.path.dirname(current_name))

filename=input("Enter the file name:")

with open(fater_dir+'/'+filename) as file:
    count =0
    for line in file:
        count+=1
        print(line,end='')
    print('Lines',count)
