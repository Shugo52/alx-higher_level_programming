#!/usr/bin/python3
"""The Rectangle module

Makes available a Rectangle class for rectangle representation
"""


class Rectangle:
    """Creates an instance of a Rectangle.

    Args:
        None

    Attributes:
        Rectangle Object/Instance
    """

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __str__(self) -> str:
        if not (self.__height and self.__width):
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def area(self) -> int:
        """Computes the area of a rectangle.

        Args:
            None

        Returns:
            Area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self) -> int:
        """Returns the perimeter of a rectangle.

        Args:
            None

         Returns:
            Perimeter of the rectangle
        """

        if self.__width and self.__height:
            return self.__width * 2 + self.__height * 2
        return 0
