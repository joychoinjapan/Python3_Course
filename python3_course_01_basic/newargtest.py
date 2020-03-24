import sys

for index, arg in enumerate(sys.argv):
    if index == 0:
        continue
    if arg.__len__() > 3:
        print(arg)
