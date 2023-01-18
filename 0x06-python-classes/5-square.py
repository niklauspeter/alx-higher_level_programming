#!/usr/bin/python3
"""class square defines a square based on 4-square.py"""


class Square:
    """class defines properties of square"""
    def __init__(self, size):
        """initializes square"""
        self.size = size

    @property
    def size(self):
        """get current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area f square"""
        return (self.size * self.size)

    def my_print(self):
        """print out a square to stdin using # character"""
        if self.size == 0:
            print("")
        for n in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        # for i in range(0, self.__size):
        #     for n in range(self.__size):
        #         [print("#", end="")]
        #         print("")
