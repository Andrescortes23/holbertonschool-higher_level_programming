#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 0 and ord(a) < 97:  # if is any other char
            print("{}".format(a), end='')
        elif ord(a) >= 97 and ord(a) < 123:  # if is lowecase
            print("{:c}".format(ord(a) - 32), end='')
    print()
