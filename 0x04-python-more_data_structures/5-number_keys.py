#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    for x in list(a_dictionary):
        if x:
           sum += 1
        else:
            return None
    return sum

#alt:
 #   return len(a_dictionry.keys())
