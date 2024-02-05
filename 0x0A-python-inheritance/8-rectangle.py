#!/usr/bin/python3
"""base geometry

"""


class BaseGeometry:
    """base geometry class"""
    def __init__(self):
        pass

    def area(self):
        """the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that validates the value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle class inherited from basegeometry"""
    def __init__(self, width, height):
        """init.new Rectangle.

        Args:
            width
            height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
