#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a text file and return the number of characters added.

Module Usage:
    $ ./2-append_write.py

"""

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the text file. Default is an empty string.
        text (str): The string to be appended to the file. Default is an empty string.

    Returns:
        int: The number of characters added to the file.

    Raises:
        None

    Example:
        nb_characters_added = append_write("example.txt", "Hello, World!\n")
        print(nb_characters_added)
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)

