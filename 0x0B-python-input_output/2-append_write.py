#!/usr/bin/python3
""""input / output

"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added
        Args:
            filename:
            text:
    """
    if not filename:
        file = open(filename, 'x')
    else:
        with open(filename, 'a') as file:
            file = file.write(text)
        return len(text)
