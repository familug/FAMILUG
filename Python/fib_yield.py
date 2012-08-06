# A python yeild example to generate fibonacci number

def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b

cntr = 0
for n in fib():
    print n
    cntr += 1
    if cntr == 10:
        break
