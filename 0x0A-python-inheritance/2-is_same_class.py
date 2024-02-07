#!/usr/bin/python3
"""
This module defines a function is_same_class.

Module Usage:
    $ ./2-main.py

"""

def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class

# Example usage
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

