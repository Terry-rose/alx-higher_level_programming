#!/usr/bin/python3
"""
Module documentation goes here
"""

class Square:
    """
    Class documentation goes here
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Method documentation goes here
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method documentation goes here
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method documentation goes here
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Method documentation goes here
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method documentation goes here
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Method documentation goes here
        """
        result = ""
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()

