#!/usr/bin/python3
""""input / output

"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object (string)
        Args:
            filename:
            text:
    """
    return json.dumps(my_obj)
