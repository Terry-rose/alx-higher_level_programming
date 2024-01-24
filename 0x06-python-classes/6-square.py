#!/usr/bin/python3

class Square:
    """
    This is the Square class.
    
    Attributes:
    - size (int): Represents the size of the square.
    - position (tuple): Represents the position of the square.
    
    Methods:
    - __init__(self, size=0, position=(0, 0)): Initializes a new Square instance.
    - size(self): Gets the size of the square.
    - size(self, value): Sets the size of the square.
    - position(self): Gets the position of the square.
    - position(self, value): Sets the position of the square.
    - area(self): Calculates and returns the area of the square.
    - my_print(self): Prints the square with the '#' character.
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
        - size (int): Represents the size of the square.
        - position (tuple): Represents the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        - value (int): The new size of the square.

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If the size is less than 0.
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
        Gets the position of the square.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
        - value (tuple): The new position of the square.

        Raises:
        - TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character.
        
        If size is equal to 0, print an empty line.
        Position should be used by using space - Don’t fill lines by spaces when position[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

