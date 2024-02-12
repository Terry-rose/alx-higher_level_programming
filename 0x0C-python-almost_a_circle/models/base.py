
#!/usr/bin/python3
"""Module containing the Base class."""

class Base:
    """Base class for managing id attribute in all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): An integer id for the instance.

        Attributes:
            id (int): The public instance attribute representing the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

