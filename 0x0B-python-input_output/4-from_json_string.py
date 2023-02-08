#!/usr/bin/python3
"""This module converts JSON string to its respective python object"""
import json


def from_json_string(my_str):
    """Makes a Python object from a JSON string

    Args:
        my_str: JSON string.

    Returns:
        A Python object. Can contain other python objects.
    """

    return json.loads(my_str)
