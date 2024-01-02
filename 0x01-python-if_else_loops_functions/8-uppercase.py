#!/usr/bin/python3
def uppercase(str):
    for str in str:
        if ord(str) in range(97, 123):
            str = chr(ord(str) - 32)
        print("{}".format(str), end="")
    print("")
