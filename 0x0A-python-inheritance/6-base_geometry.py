#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a public instance method area.

Module Usage:
    $ ./6-main.py

"""

class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

# Example usage
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

