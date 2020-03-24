# for循环和while循环
strList = ['hello', 'shiyanlou', '.com']
for s in strList:
    print(s)

print('----------------------')
# range()
for a in range(3, 10, 3):
    print(a)

# while 循环
w = 100
while w > 10:
    print(w)
    w -= 10
print('----------------------')
# 我们在循环控制中，可以使用 break 和 continue 两个关键字，
# break 表示停止当前循环，continue 表示跳过当前循环轮次中后续的代码，去执行下一循环轮次。
w = 100
while w > 10:
    w -= 10
    if w == 50:
        continue
    print(w)



