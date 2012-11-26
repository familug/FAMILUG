# A python yeild example to generate fibonacci number

def fib(n):
    cntr = 0
    a, b = 0, 1
    while cntr < n:
        yield a
        a, b = b, a + b
        cntr += 1
        
for i in fib(10):
    print i
