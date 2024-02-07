#!/usr/bin/python3

class BaseGeometry:
    """
    This module defines a class Square that inherits from Rectangle.

Instantiation with size and implementation of the area method.

Module Usage:
    $ ./10-main.py
    """

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the given value.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with the specified width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("_Rectangle__width", width)
        self.integer_validator("_Rectangle__height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a square with the specified size.

        Args:
            size: The size of the square.
        """
        self.integer_validator("_Square__size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

# Example usage
if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

