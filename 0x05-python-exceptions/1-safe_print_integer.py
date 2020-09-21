#!/usr/bin/python3
def safe_print_integer(value):
    cast = str(value)
    try:
        if ord(cast[0]) < 58 and ord(cast[0]) > 47 or ord(cast[0]) == 45:
            print("{:d}".format(value))
            return (True)
    except:
        return False
