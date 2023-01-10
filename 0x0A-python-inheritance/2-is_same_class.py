#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    function returns true if object
    is exactly an instance of specified
    class
    """

    if type(obj) == a_class:
        return True
    else:
        return False
