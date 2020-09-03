#!/usr/bin/python3
import sys

arglen = len(sys.argv) - 1  # To argv doesnt count my function as arg
print("{} ".format(arglen), end='')

if arglen == 0:
    print("{}".format("arguments."))
elif arglen == 1:
    print("{}".format("argument:"))
elif arglen > 1:
    print("{}".format("arguments:"))

iterator = 1
while iterator != arglen + 1:
    print("{}: {}".format(iterator, sys.argv[iterator]))
    iterator = iterator + 1
