#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Rectangle class with width and height attributes
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of Rectangle

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for width

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: The string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle for reproduction

        Returns:
            str: The string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method for Rectangle

        Prints a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

if __name__ == "__main__":
    # Example usage
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

