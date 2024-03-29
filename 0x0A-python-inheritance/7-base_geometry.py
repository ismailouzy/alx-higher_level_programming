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
        self.value = value
        self.name = str(name)

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
