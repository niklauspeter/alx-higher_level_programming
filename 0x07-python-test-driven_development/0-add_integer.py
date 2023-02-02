#!/usr/bin/python3
"""function adds two integers"""

def add_integer(a, b=98):
    """function takes in two integers and adds them
    
    float args are typecasted to ints before addition is performed
    
    Raises:
            TypeError is a or b is not int or not float"""

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
