g=(x**x for x in range(1,7))
for x in g:
    print(x)


def fib(n):
    current =0
    a,b =1,1
    while current < n:
        yield a
        a,b =b,a+b
        current +=1

f5=fib(10)

for x in f5:
    print(x)