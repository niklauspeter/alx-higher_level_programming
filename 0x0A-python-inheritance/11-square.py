#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # def area(self, size):
    #     return self.__size * self.__size

    # def str(self, size):
    #     """Return the print() and str() representation of a Rectangle."""

    #     string = "[" + str(self.__class__.__name__) + "] "
    #     string += str(self.__size) + "/" + str(self.__size)
    #     return string
