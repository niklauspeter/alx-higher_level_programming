#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """returns elements that are not common in two sets"""
    return (set_1 ^ set_2)
