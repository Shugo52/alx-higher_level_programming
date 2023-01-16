#!/usr/bin/python3
"""Base module."""


class Base:
    """Base class. Provides a Base class for subsequent Classes

    Attributes:
        nb_objects (private): Keeps track of all instances of the base class.

    Args:
        id: Public instance id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
