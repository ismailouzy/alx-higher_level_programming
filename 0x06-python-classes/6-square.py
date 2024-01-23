#!/usr/bin/python3


"""Class square"""


class Square:
    """Class square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize function
        args:
            size: size of square
            position: position of square"""
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """my print function"""
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
            return

    @property
    def position(self):
        """ set the area"""
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(n) is not int for n in value) or any(a < 0 for a in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
