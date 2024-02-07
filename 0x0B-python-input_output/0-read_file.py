#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a text file.

Module Usage:
    $ ./0-read_file.py

"""

def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the text file to be read. Default is an empty string.

    Returns:
        None

    Raises:
        None

    Example:
        read_file("example.txt")
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")

if __name__ == "__main__":
    read_file("my_file_0.txt")

