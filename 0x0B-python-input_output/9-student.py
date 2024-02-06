#!/usr/bin/python3
"""input output

"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Init new Student
        Args:
            first_name:
            last_name:
            age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student
        """
        return self.__dict__
