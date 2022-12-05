#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
   """prints list in reverse"""
   if isinstance(my_list, list):
      # last_index = (len(my_list) - 1)
       #for i in my_list:
        #   if last_index >= 0:
         #      print ("{:d}".format(my_list[last_index]))
          #     last_index = last_index - 1
      my_list.reverse()
      for i in my_list:
          print("{:d}".format(i))
