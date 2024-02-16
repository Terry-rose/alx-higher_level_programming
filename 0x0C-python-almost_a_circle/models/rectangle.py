#!/usr/bin/python3
"""Module containing the Rectangle class."""

class Rectangle:
    """Rectangle class with width, height, x, y, and id attributes."""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle (default is 0).
            y (int): Y-coordinate of the rectangle (default is 0).
            id (int): ID of the rectangle (default is None).

        Attributes:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): ID of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id if id is not None else self.__generate_id()

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__validate_positive_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__validate_positive_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__validate_non_negative_int("y", value)
        self.__y = value

    @property
    def id(self):
        """Getter for the id attribute."""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter for the id attribute."""
        self.__validate_positive_int("id", value)
        self.__id = value

    def __validate_positive_int(self, attribute, value):
        """Validate that a value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be a positive integer".format(attribute))

    def __validate_non_negative_int(self, attribute, value):
        """Validate that a value is a non-negative integer."""
        if not isinstance(value, int) or value < 0:
            raise TypeError("{} must be a non-negative integer".format(attribute))

    def __generate_id(self):
        """Generate a new ID."""
        Rectangle.__nb_objects += 1
        return Rectangle.__nb_objects

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign arguments to attributes.

        Args:
            *args: Arguments passed as positional arguments.
            **kwargs: Arguments passed as keyworded arguments.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

