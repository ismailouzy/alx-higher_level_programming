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
        self.__width = width
        self.__height = height

    @property
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
