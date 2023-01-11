#!/usr/bin/python3
"""
raises errors
"""

def area(self):
    """raises exception"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    if type(value) not "int":
        Exception TypeError:
        print("{} must be an integer".format(name))
    if value <= 0:
        Exception ValueError:
        print("{} must be greater than 0".format(name))