#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return float(a / b)
    except ZeroDivisionError:
        return None
    finally:
        if a == 0 or b == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(a / b))
