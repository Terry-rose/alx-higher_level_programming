#!/usr/bin/python3
"""
Module documentation goes here
"""

class BaseGeometry:
    """
    Class documentation goes here
    """

    def area(self):
        """
        Method documentation goes here
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method documentation goes here
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

