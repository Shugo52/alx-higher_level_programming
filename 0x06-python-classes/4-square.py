#!/usr/bin/python3

"""Defines a Square class."""


class Square():
    """Defines a Square class."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__init__(value)

    def area(self):
        """Calculates the area of a square"""

        return self.__size ** 2
