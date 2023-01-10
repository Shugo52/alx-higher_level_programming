#!/usr/bin/python3
"""Base geometry module."""


class BaseGeometry:
    """Geometry class."""

    def area(self):
        """Raises an exception when called."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer input"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
