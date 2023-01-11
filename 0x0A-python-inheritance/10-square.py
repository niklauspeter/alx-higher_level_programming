#!/usr/bin/python3
"""class square inherits from rectangle"""

Rectangle = __import__("9-rectangle.py").Rectangle

class Square(Rectangle):
    """sintantiates size of sides of square"""

    def __init__(self, size):
        """reps a square"""


        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    #def area(self):
    #    return self.__size * self.__size
    
    #def __str__(self):
     #   """Return the print() and str() representation of a Rectangle."""
      #  string = "[" + str(self.__class__.__name__) + "] "
       # string += str(self.__size) + "/" + str(self.__size)
        #return string