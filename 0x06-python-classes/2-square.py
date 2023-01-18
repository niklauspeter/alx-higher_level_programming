#!/usr/bin/python3
"""class defines a square"""


class Square:
    """create private attribute size.
    args:
    size must be int - else raise type error
    size must be less than 0 - elese raise exception error"""

    def __init__(self, size=0):
        """initialize a new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size       