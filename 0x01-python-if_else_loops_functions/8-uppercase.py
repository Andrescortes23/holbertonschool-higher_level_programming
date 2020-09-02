#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) == 32:  # if is space char
            print("{}".format(a), end='')
        elif ord(a) >= 48 and ord(a) < 58:  # if is a number
            print("{}".format(a), end='')
        elif ord(a) >= 97 and ord(a) < 123:  # if is lowecase
            print("{:c}".format(ord(a) - 32), end='')
        elif ord(a) > 64 and ord(a) < 91:  # if is a uppercase
            print("{}".format(a), end='')
    print()
