#!/usr/bin/python3

"""defines a class rectangle which inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """initialize a new rectangle"""
        

        super().integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    print("[Rectangle] {}/{}".format(self.width,self.length))

    def area(self):
        A = self.width * self.length
        return str(A)