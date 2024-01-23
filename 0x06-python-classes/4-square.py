#!/usr/bin/python3

"""Class square"""


class Square:
    def __init__(self, size=0):
        """initialize function
        args:
            size: size of square"""
        self.__size = size

    def area(self):
        """initialize area"""
        return self.__size**2

    @property
    def size(self):
        """property size function"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter for size function
        args:
            value: value of the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
