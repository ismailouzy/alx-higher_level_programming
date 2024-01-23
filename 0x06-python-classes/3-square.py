#!/usr/bin/python3

"""Class square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """initialize function
        Args:
            size: size of square"""
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """initialize area"""
        return self.__size
