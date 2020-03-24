import sys
sys.argv.pop(0)
new_set=set(sys.argv)
new_list=[]
for item in new_set:
    new_list.append(item)
print(' '.join(new_list))