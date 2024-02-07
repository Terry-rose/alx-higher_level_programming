#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list and then saves them to a file using JSON representation.

Script Usage:
    $ ./7-add_item.py [arg1] [arg2] [arg3] ...

"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list_and_save(args):
    """
    Add command line arguments to a Python list and save them to a file using JSON representation.

    Args:
        args (list): A list of command line arguments.

    Returns:
        None

    Raises:
        None
    """
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    new_items = existing_items + args

    save_to_json_file(new_items, "add_item.json")

if __name__ == "__main__":
    args = sys.argv[1:]
    add_items_to_list_and_save(args)

