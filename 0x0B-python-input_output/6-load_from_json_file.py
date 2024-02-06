#!/usr/bin/python3
""""input / output

"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a 'JSON file'
        Args:
            filename:
    """
    with open(filename, "r") as file:
        return json.load(file)
