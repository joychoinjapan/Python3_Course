import sys
list_1=[]
list_2=[]
for arg in sys.argv[1:]:
    arg=str(arg)
    if arg.__len__()<=3:
        list_1.append(arg)
    else:
        list_2.append(arg)
print(' '.join(list_1))
print(' '.join(list_2))
