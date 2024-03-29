#!/usr/bin/python3

"""Defines a Square class."""


class Square():
    """Defines a Square class."""

    def __init__(self, size=0):
        if int is not type(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
