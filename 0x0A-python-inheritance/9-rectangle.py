#!/usr/bin/python3

"""defines a class rectangle which inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """initialize a new rectangle"""

        super().integer_validator("width", width)
        super().__width = width
        super().integer_validator("height", height)
        super().__height = height

    def area(self):
        A = self.width * self.length
        return A

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
