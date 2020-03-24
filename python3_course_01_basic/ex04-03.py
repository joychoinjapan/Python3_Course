#终端运行Python程序
#命令行参数
import sys
print(len(sys.argv))
for arg in sys.argv:
    print(arg)

#$ python3 ex04-03.py hello shiyanlou
#输出如下
#3
#ex04-03.py
#hello
#shiyanlou