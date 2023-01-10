#!/usr/bin/python3
"""Defines a class-checking functino ."""

def is_same_class(obj, a_class):
    """'''
    function: is_same_class
    obj: an object
    a_class: a class
    returns: Bool
    """

    if type(obj) == a_class:
        return True
    else:
        return False
