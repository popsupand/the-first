def fib(x, y):
    a, b = 1, 1
    fb = []
    while a < y:
        if a >= x:
            fb.append(a)
        a, b = b, a + b
    if fb:
        print('Fibonacci numbers:', *fb)
    else:
        print('Fibonacci numbers: none found')

def cov(x, y):
    lst = []
    for i in range(x, y+1):
        s = 0
        for j in range(1, i+1):
            if i % j == 0 and j != i:
                s += j
        if s == i:
            lst.append(i)
    if lst:
        print('Perfect numbers:', *lst)
    else:
        print('Perfect numbers: none found')

def arm(x, y):
    sp = []
    for i in range(x, y):
        n = len(str(i))
        st = list(str(i))
        s = 0
        for j in st:
            d = int(j)
            s += d**n
        if i == s:
            sp.append(i)
    if sp:
        print('Armstrong numbers:',*sp)
    else:
        print('Armstrong numbers: none found')



print("Enter the start and end of the interval:")
a = int(input('a = '))
b = int(input('b = '))
fib(a, b)
cov(a, b)
arm(a, b)
