#!/usr/bin/python3
"""defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of class

    obj: the object to check
    a_class: the class to match the type of obj
    returns:true if obj is an instance false if not
    """
    if isinstance(obj, a_Class):
        return True
    return False
