#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
   # fin_list = []
    #fin_list.append(replace) if x == search else fin_list.append(x) for x in my_list
    #return fin_list
    return [val if val != search else replace for val in my_list]
