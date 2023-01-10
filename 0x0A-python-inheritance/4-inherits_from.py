#!/usr/bin/python3
"""Inherits from class"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class inheriting directly
    or indirectly from a_class
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
