#!/usr/bin/python3
"""the almighty square

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str function"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square
        Args:
            @args:
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
