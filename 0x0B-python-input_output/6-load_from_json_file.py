#!/usr/bin/python3
"""
This module provides a function to create an object from a JSON file.

Module Usage:
    $ ./6-load_from_json_file.py

"""

import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the JSON file does not represent a valid object.

    Example:
        filename = "example.json"
        my_dict = load_from_json_file(filename)
        print(my_dict)
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    except ValueError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except ValueError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

