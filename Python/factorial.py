def factorial(n):
    ret = [1]

    # edge condition
    fact = 1
    # must know number of running
    for i in range(1,n + 1):
        fact *= i
        ret.append(fact)

    return ret

def mfac_recursive2(n):
    def sfac_recursive(n):
        # single factorial
        # edge condition
        if n == 0:
            return 1
        else:
            return n * sfac_recursive(n - 1) 

    ret = []
    for i in range(0, n + 1):
        ret.append(sfac_recursive(i))
    return ret

def mfac_recursive3(n):
    ret = []

    def sfac_recursive(n):
        # single factorial
        # edge condition
        if n == 0:
            return 1
        else:
            return n * ret[n - 1]

    for i in range(0, n + 1):
        ret.append(sfac_recursive(i))
    return ret

print factorial(5)
print mfac_recursive2(5)
print mfac_recursive3(5)
