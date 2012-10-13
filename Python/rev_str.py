def reverse_str1(astring):
    iter = reversed(astring)
    return "".join(iter)
    

def reverse_str2(astring):
    return astring[::-1]


def main():
    STRING = "HVNSWEETING"
    print reverse_str1(STRING)
    print reverse_str2(STRING)

if __name__ == "__main__":
    main()
