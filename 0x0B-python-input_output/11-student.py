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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        """
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            stu_dict = {}
            for j in attrs:
                if hasattr(self, j):
                    stu_dict[j] = getattr(self, j)
            return stu_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
            Args:
                json:
        """
        for ke, valeur in json.items():
            setattr(self, ke, valeur)
