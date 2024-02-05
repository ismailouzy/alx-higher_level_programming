#!/usr/bin/python3
"""can i

"""


def add_attribute(obj, name, value):
    """ a function that adds a new attribute
    to an object if it’s possible
        Args:
            obj:
            name:
            value:
    """
    if not hasattr(obj, '__dict__') and not isinstance(obj, object):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
