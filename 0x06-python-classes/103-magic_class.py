#!/usr/bin/python3
import math

class MagicClass:
    """
    A class representing a Magic Circle with radius-based calculations.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Parameters:
        - radius (float or int): The radius of the Magic Circle.

        Raises:
        - TypeError: If the provided radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates the area of the Magic Circle.

        Returns:
        - float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the Magic Circle.

        Returns:
        - float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius

