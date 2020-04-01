filename="shiyanlou.txt"
file=open(filename)
lines=file.readlines()
file.close()

filename="shiyanlou_copy.txt"

for index,line in enumerate(lines):
    with open(filename, 'a') as file:
        file.write('{} {}'.format(index+1,line))
