#!/usr/bin/bash
"""function returns true if
object is instance of class inherited from a specified
class"""


def inherits_from(obj, a_class):
    """checks if object is instance of a class that inherited
    obj : the oject in question
    a_class: class being compared
    returns: true if obj inherited from class
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
