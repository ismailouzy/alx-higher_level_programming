#!/usr/bin/python3
"""Base class

"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        list_dictionaries
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            with open("{}.json".format(cls.__name__), "w") as file:
                compreh = [ob.to_dictionary() for ob in list_objs]
                file.write(cls.to_json_string(compreh))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummydummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummydummy = cls(1)
        dummydummy.update(**dictionary)
        return dummydummy

    @classmethod
    def load_from_file(cls):
        """a list of instances"""
        smiya = f"{cls.__name__}.json"
        try:
            with open(smiya, "r") as file:
                data = file.read()
                dictionaries = json.loads(data)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []
