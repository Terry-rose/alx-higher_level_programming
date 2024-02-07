#!/usr/bin/python3
"""
This module provides a function to write a string to a text file and return the number of characters written.

Module Usage:
    $ ./1-write_file.py

"""

def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the text file. Default is an empty string.
        text (str): The string to be written to the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        None

    Example:
        nb_characters = write_file("example.txt", "Hello, World!\n")
        print(nb_characters)
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

