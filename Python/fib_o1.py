from math import sqrt

def fib(n):
    sqrt5 = sqrt(5)
    term_one = ((1 + sqrt5) / 2) ** n
    term_two = ((1 - sqrt5) / 2) ** n
    return int((term_one - term_two) / sqrt5)

for i in range(100):
    print i, fib(i)
