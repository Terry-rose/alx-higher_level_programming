#!/usr/bin/python3
"""Test script for the Base class."""
from models.base import Base

if __name__ == "__main__":
    # Test cases
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
