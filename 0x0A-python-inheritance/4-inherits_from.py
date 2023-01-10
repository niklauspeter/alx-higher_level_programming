#!/usr/bin/bash
"""function returns true if
object is instance of class inherited from a specified
class"""


def inherits_from(obj, a_class):
    """
    obj : the oject in question
    a_class: class being compared
    returns: true if obj inherited from class
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
