#!/usr/bin/python3
def uppercase(str):
    for str in str:
        if ord(str) in range(97, 123):
            print(chr(ord(str)-32), end="")
        else:
            print(str, end="")      
    print()
