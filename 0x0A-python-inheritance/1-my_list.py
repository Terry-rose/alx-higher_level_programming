#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.

Module Usage:
    $ ./1-main.py

"""

class MyList(list):
    """A custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

# Example usage
if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)
    my_list.print_sorted()
    print(my_list)

