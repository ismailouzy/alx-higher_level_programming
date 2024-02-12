#!/usr/bin/python3
"""First rectangle

"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base"""

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.inst_validator_equal("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.inst_validator_equal("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.inst_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.inst_validator("y", y)
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor
            Args:
                @width: width of the rectangle
                @height: height of the rectangle
                @x(int):
                @y(int):
                @id: None
        """
        super().__init__(id)
        self.inst_validator_equal("width", width)
        self.__width = width
        self.inst_validator_equal("height", height)
        self.__height = height
        self.inst_validator("x", x)
        self.__x = x
        self.inst_validator("y", y)
        self.__y = y

    def inst_validator_equal(self, name, value):
        """setter methods and instantiation validator
        Args:
            @name:
            @value:
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be > 0")

    def inst_validator(self, name, value):
        """setter methods and instantiation validator
        Args:
            @name:
            @value:
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints the stdout of the rectangle"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle
        Args:
            @args: variable number of
            arguments in the order id, width, height, x, y
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representation of a Rectangle"""
        return {"y": self.y, "x": self.x,
                "id": self.id, "width": self.width, "height": self.height}
