#!/usr/bin/python3
def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to inspect.

    Returns:
    - A list containing the names of attributes and methods of the object.
    """
    return [attr for attr in dir(obj)]

