# Run Length Encoding
# The manual version and other version using groupby
# See http://rosettacode.org/wiki/Run-length_encoding#Python for groupby

import itertools


def rle(string):
    if string == '':
        raise ValueError("string must not empty")

    print("*Input: %s" % string)

    prev_c = string[0]
    print("--Processing index 0 char %s" % prev_c)
    count = 1
    out = []

    for idx in range(1, len(string)):
        c = string[idx]
        print("--Processing index %d char %s" % (idx, c))
        if c == prev_c:
            count += 1
            print("    It is the same char as the previous one, count %s: %d" % (c, count))  # NOQA
        else:
            out.append(prev_c + str(count))
            print("    Result now: %s" % out)
            print("    Got new char: %s, set counter to 1" % c)
            count = 1
            prev_c = c

    print("--No more character, add the last char+count to result")
    out.append(c + str(count))
    print("    Result now: %s" % out)
    result = ''.join(out)

    print("*Output: %s\n" % result)

    return result


def rle_groupby(string):
    out = []
    for c, group in itertools.groupby(string):
        out.append(c + str(len(list(group))))
    return ''.join(out)


if __name__ == "__main__":
    for case, expect in [
        ("aaaaa", "a5"), ("aabbcc", "a2b2c2"), ("aaac", "a3c1")
    ]:
        res = rle(case)
        assert res == rle_groupby(case) == expect, (case, res, expect)
