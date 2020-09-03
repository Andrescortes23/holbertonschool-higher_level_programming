#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arglen = len(sys.argv) - 1

    iterator = 1
    while iterator != arglen + 1:
        if iterator > 1:
            buf = buf + int(sys.argv[iterator])
        elif iterator == 1:
            buf = (int(sys.argv[iterator]))
        iterator += 1
    if iterator > 1:
        print(buf)
    else:
        print("0")
