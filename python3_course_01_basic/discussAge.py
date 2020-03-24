import sys
Age = int(sys.argv[1])

if Age>= 0 and Age < 10:
    print('you belong to kids')
elif Age>= 10 and Age < 18:
    print('you belong to teenager')
elif Age >= 18 and Age < 30:
    print('you belong to adult')
elif Age>= 30 and Age < 60:
    print('you belong to older')
elif Age>= 60 and Age < 120:
    print('you belong to oldest')
