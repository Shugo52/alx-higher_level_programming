#!/usr/bin/python3
"""Rectange module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class.

    Args:
        size: Length of sides.
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """Calculates square area."""

        return self.__size**2
