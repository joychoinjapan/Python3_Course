# 异常处理方式

filename = input("Enter file path:")
try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError as err:
    print("File not found error")
finally:
    print("finally")
