#!/usr/bin/python3
"""
class list inherits from list
"""


class MyList(list):
    """
    represents a list
    """

    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
