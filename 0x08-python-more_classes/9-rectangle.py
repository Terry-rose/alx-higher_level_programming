#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Rectangle class with width, height, class attributes, and methods
    """

    number_of_instances = 0
    print_symbol = "#"

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
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to compare two rectangles based on area

        Args:
            rect_1 (Rectangle): The first rectangle to compare
            rect_2 (Rectangle): The second rectangle to compare

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: The rectangle with the larger area or rect_1 if both have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method to create a square rectangle

        Args:
            size (int): The size of the square. Default is 0.

        Returns:
            Rectangle: A new instance of Rectangle with equal width and height
        """
        return cls(size, size)


if __name__ == "__main__":
    # Example usage
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)

