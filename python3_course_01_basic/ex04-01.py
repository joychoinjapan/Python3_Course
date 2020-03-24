#条件判断
a=int(input("Please Enter"))
if a>10:
    print ('a>10')
elif a==10:
    print ('a=10')
else:
    print ('a<10')


b=int(input("Please Enter"))
#嵌套的条件判断
if b>10:
    if b>=30:
        print('b>=30')
    else:
        print ('10<b<30')
else:
    print('b<10')



