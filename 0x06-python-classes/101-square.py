#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self) -> str:

        square = ""

        if not self.__size:
            return ""

        # Print (lines * position[1])
        for _ in range(self.__position[1]):
            square += "\n"

        # Print square with each line preceeded by (space * position[0])
        for unit in range(self.__size):
            square += f"{' ' * self.__position[0]}{'#' * self.__size}"
            square += "\n" if unit+1 < self.__size else ""

        return square

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or not len(value) == 2
            or not all(isinstance(i, int) for i in value)
            or min(value) < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square"""

        return self.__size**2

    def my_print(self):
        """Prints a square to stdout"""

        if not self.__size:
            print()
            return

        # Print (lines * position[1])
        for _ in range(self.__position[1]):
            print()

        # Print square with each line preceeded by (space * position[0])
        for _ in range(self.__size):
            print(f"{' ' * self.__position[0]}{'#' * self.__size}")
