#!/usr/bin/python3
"""read file

"""


def read_file(filename=""):
    """a fucntion that reads a text file
        Args:
            filename:
    """
    with open(filename, "r", encoding="UTF-8") as file:
        content = file.read()
    print(content)
