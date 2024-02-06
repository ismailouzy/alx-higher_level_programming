#!/usr/bin/python3


def read_file(filename=""):
    """a fucntion that reads a text file
        Args:
            filename:
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content)
