#!/usr/bin/python3
"""
Module documentation goes here
"""

class Square:
    """
    Class documentation goes here
    """
    def __init__(self, size=0):
        """
        Method documentation goes here
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method documentation goes here
        """
        return self.__size ** 2

