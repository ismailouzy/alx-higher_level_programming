#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """a class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle
        with the specified width and height.

        Args :
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area of the rectangle"""
        return self.__width*self.__height

    def perimeter(self):
        """the perimeter of the rectangle"""
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        return (self.__width + self.__height)*2

    def __str__(self):
        """str """
        if self.__width == 0:
            return ""
        elif self.__height == 0:
            return ""
        ster = str(self.print_symbol) * self.width
        return (ster + "\n") * (self.height - 1) + ster

    def __repr__(self):
        """repr"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
