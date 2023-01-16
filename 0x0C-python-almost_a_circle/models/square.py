#!/usr/bin/python3
"""Square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class that inherits from the Rectangle class.

    Args:
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Prints the rectangle instance.

        Returns:
            Representation of instance.
        """

        return (
            f"[{self.__class__.__name__}] "
            f"({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )
