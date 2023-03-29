#!/usr/bin/python3
""" Student class Module"""


class Student:
    """ Defines a Student class

    Attributes:
        None
    """
    def __init__(self, first_name, last_name, age):
        """ Defines init method of student class

        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Defines to json method of student class

        Args:
            None

        Returns:
            Dictionary representation of student class
        """
        return self.__dict__
