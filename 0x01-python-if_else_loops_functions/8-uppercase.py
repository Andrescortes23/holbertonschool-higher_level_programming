#!/usr/bin/python3
def uppercase(str):
    for a in str:
        a = ord(a)
        if a >= 97 and a < 123:  # if is lowecase
            a = a - 32
        print("{:c}".format(a), end='')
    print()
