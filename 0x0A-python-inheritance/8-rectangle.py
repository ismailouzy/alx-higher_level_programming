#!/usr/bin/python3
"""base geometry

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
