#!/usr/bin/python3
"""Kind of class module."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an exact instance of a_class."""

    if isinstance(obj, a_class):
        return True
    return False
