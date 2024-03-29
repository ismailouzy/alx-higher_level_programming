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


class Rectangle(BaseGeometry):
    """rectangle class inherited from basegeometry"""
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """a subclass square from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
