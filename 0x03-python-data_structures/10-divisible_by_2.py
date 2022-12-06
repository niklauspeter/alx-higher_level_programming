#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """functino finds all multiples of two in a list"""
    if my_list == "":
        return (None)
    
    multiples_list = []
    
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_list.append(True)
        else:
            multiples_list.append(False)
    
    return multiples_list
