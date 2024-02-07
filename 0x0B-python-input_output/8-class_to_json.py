#!/usr/bin/python3
"""
This module provides a function to return the dictionary description with a simple data structure for JSON serialization of an object.

Module Usage:
    $ ./8-class_to_json.py

"""

def class_to_json(obj):
    """
    Return the dictionary description with a simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description with a simple data structure.

    Raises:
        None
    """
    attributes = obj.__dict__
    new_dict = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            new_dict[key] = value
    return new_dict

if __name__ == "__main__":
    pass 

