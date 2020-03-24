num = input("Enter number:")
try:
    new_num = int(num)
    print('INT:{}'.format(new_num))
except ValueError as error:
    print('ERROR:{}'.format(num))



