def pascal_row(row):
    ret = []
    def one_elem(r, c):
        # Vc = Vc-1 * (r - c) / c , r = row + 1, V0 = 1
        if c == 0:
            return 1
        else:
            return one_elem(r, c - 1) * (r - c)/ c
    r = row + 1
    for i in range(r):
        ret.append(one_elem(r, i))
    return ret


    

def pascal(row):
    ret = [1]
    # edge condition c0 = 1
    col = 1

    r = row + 1
    for i in range(1, r):
        col *= (r - i)
        col /= i
        ret.append(col)

    return ret

if __name__ == "__main__":
    for i in range(7):
        print pascal(i)
        print pascal_row(i)
