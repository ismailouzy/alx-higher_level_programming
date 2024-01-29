#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle
        with the specified width and height.

        Args :
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
