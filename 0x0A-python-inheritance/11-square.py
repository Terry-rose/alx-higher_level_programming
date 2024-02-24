#!/usr/bin/python3
"""
Module documentation goes here
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class documentation goes here
    """

    def __init__(self, size):
        """
        Method documentation goes here
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Method documentation goes here
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method documentation goes here
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

