#!/usr/bin/python3
"""Rectangle module."""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class that inherits from the Base class.

    Args:
        width: Rectangle width.
        height: Rectangle height.
        x: x value
        y: y value
        id: Public instance id"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Setter/getter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")

        self.__width = value

    # Setter/getter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 1:
            raise ValueError("height must be > 0")

        self.__height = value

    # Setter/getter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Setter/getter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Computes the area of the rectangle.

        Returns:
            Rectangle area.
        """

        return self.__height * self.__width

    def __str__(self) -> str:
        """Prints the rectangle instance.

        Returns:
            Representation of instance.
        """

        return (
            f"[{self.__class__.__name__}] "
            f"({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def display(self):
        """Prints the rectangle with the "#" character, ofsetting by x & y."""

        for _ in range(self.__y):
            print("")

        for _ in range(self.__height):
            print(f"{' ' * self.__x}{'#' * self.__width}")

    def update(self, *args, **kwargs):
        """Assigns args to instance attributes."""

        attr = ('id', 'width', 'height', 'x', 'y')

        for i in range(len(args)):
            setattr(self, attr[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)
