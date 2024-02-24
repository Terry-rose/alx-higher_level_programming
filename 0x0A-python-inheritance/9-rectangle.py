#!/usr/bin/python3
"""
Module documentation goes here
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class documentation goes here
    """

    def __init__(self, width, height):
        """
        Method documentation goes here
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method documentation goes here
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method documentation goes here
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

