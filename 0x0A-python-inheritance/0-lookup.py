#!/usr/bin/python3
"""Lookup module"""


def lookup(obj=None):
    """Returns a list of the available attributes of an object.

    Args:
        obj: Object to lookup attribute.

    Return:
        List of attributes available to an object.
    """

    return dir(obj)


if __name__ == "__main__":
    lookup()
