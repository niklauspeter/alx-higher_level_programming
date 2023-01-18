#!/usr/bin/python3
"""class defines a square"""


class Square:
    """defines a square(based on 3-square.py)"""
    def __init__(self, size=0):
        """initialize a new square"""

        self.size = size

    @property
    def size(self):
        """returns current area of the square"""
        return self.__square

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)