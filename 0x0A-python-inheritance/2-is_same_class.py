#!/usr/bin/python3
"""Same class module."""


def is_same_class(obj, a_class):
    """Returns True if obj is an exact instance of a_class."""

    if type(obj) is a_class:
        return True
    return False
