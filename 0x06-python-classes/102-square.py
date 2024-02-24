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
        self.size = size

    @property
    def size(self):
        """
        Getter method documentation goes here
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method documentation goes here
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Method documentation goes here
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Method documentation goes here
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Method documentation goes here
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Method documentation goes here
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Method documentation goes here
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Method documentation goes here
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Method documentation goes here
        """
        return self.area() >= other.area()

