#!/usr/bin/python3
def uppercase(str):
    """
    A function that prints a string in uppercase
    """
    string = ""
    for i in str:
        if ord(i) in range(97, 123):
            string += chr(ord(i) + 32)
        else:
            string += i
    return string
