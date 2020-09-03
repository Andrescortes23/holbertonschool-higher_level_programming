#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    import sys

    arglen = len(sys.argv)
    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])

    if arglen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sign == '+':
            print("{} {} {} = {}".format(a, sign, b, c.add(a, b)))
        elif sign == '-':
            print("{} {} {} = {}".format(a, sign, b, c.sub(a, b)))
        elif sign == "*":
            print("{} {} {} = {}".format(a, sign, b, c.mul(a, b)))
        elif sign == '/':
            print("{} {} {} = {}".format(a, sign, b, c.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
