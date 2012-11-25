def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib_fast(n):
    from math import sqrt
    s5 = sqrt(5)
    x = ((1 + s5) / 2) ** n
    y = ((1 - s5) / 2) ** n
    return int((x - y)/s5)
    

def print_fib(n):
    for i in range(n):
        print fib(i),
    print
    for i in range(n):
        print fib_fast(i),


def print_fib2(n):
    fibs = [0, 1]
    a, b = 0, 1
    if n == 0:
        print a
    elif n == 1:
        print a, b
    else:
        print 0, 1, 
        for i in range(2, n):
            c = a + b
            a, b = b, c
            print c,


if __name__ == "__main__":
    print_fib(10)
    print 
    print_fib2(10)
