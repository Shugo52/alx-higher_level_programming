#!/usr/bin/python3

"""Defines a Square class."""


class Square():
    """Defines a Square class."""

    def __init__(self, size=0):
        self.size = size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ne__(self, other):
        return self.size != other.size

    def __eq__(self, other):
        return self.size == other.size

    @property
    def size(self):
        """Getter property for __size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates the area of a square"""

        return self.__size ** 2
