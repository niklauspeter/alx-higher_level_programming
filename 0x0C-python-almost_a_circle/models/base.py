#!.usr/bin/python3
"""class will be base of other classes in the project"""


class Base:
    """instantiates by increasing number of objects"""
    __nb_object = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object