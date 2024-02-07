#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int.

MyInt is a rebel. MyInt has == and != operators inverted.

Module Usage:
    $ ./100-main.py
"""

class MyInt(int):
    """A class representing an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)

# Example usage
if __name__ == "__main__":
    my_i = MyInt(3)

    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

