#!/usr/bin/python3


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written
        Args:
            filename:
            text:
    """
    if not filename:
        file = open(filename, 'x')
    else:
        with open(filename, 'w') as file:
            file = file.write(text)
        return len(text)
