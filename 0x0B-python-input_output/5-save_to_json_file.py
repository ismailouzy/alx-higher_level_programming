#!/usr/bin/python3
""""input / output

"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to
    a text file, using a JSON representation
        Args:
            my_obj:
            filename:
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
