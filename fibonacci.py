def fib(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    print(a, b, end=' ')
    while n-2 > 0:
        c = a + b
        print(c, end=' ')
        a, b = b, c
        n -= 1

fib(10)


print("Hey dev 1")
print("Hey dev 2 made another change")