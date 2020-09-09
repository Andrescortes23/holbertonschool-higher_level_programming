#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        Firstchar = None
        Length = len(sentence)
    else:
        Length = len(sentence)
        Firstchar = sentence[0]

    newtuple = (Length, Firstchar)

    return (newtuple)
