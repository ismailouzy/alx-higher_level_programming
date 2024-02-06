#!/usr/bin/python3
""""input / output

"""
import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string
        Args:
            my_str:
    """
    return json.loads(my_str)
