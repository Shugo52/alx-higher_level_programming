#!/usr/bin/python3
""" class to json Module"""

import json


def class_to_json(obj):
    """ Returns a python object representation of an object instance

    Args:
        obj: object instance

    Returns:
        dictionary representation of an object instance
    """
    return obj.__dict__
