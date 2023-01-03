#!/usr/bin/python3
"""The print square module."""


def print_square(size=0):
    """Prints a square to stdout.

    Args:
        size (int): Length of square sides.

    Returns:
        None.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
