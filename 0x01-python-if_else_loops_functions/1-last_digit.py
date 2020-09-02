#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = "and is less than 6 and not 0"
greater = "and is greater than 5"

if number > 0:
    if number % 10 > 5:
        print("Last digit of", number, "is", number % 10, greater)
    elif number % 10 < 6:
        print("Last digit of", number, "is", number % 10, less)
    elif number % 10 == 0:
        print("Last digit of", number, "is", number % 10, "and is 0")

if number < 0:
    if number % 10 == 0:
        print("Last digit of {} is {} and is 0".format(number, number % 10))

    else:
        print("Last digit of", number, "is", (-((abs(number) % 10))), less)

if number == 0:
    print("Last digit of", number, "is", number % 10, "and is 0")
