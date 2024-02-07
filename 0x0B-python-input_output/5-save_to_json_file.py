#!/usr/bin/python3
"""
This module provides a function to write an object to a text file using a JSON representation.

Module Usage:
    $ ./5-save_to_json_file.py

"""

import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the text file.

    Returns:
        None

    Raises:
        None

    Example:
        filename = "example.json"
        my_dict = {"key": "value"}
        save_to_json_file(my_dict, filename)
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = { 132, 3 }
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

