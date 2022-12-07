#!/usr/bin/python3
from time import sleep
def magic_tree():
    a = 1
    b = 0
    c = 1
    list1 = []
    spaces = [" "]
    spaces_num = 9

    for i in range(9):
        b += 1
        list1.append(a)
       # print(list1)
        list2 = [str(i) for i in list1]
        list3 = "".join(list2)
        #spaces2 = [str(i) for i in spaces]
        spaces3 = "".join(spaces)
       # print(list3)
        print("{}{} * 8 + {} = {}".format(spaces3*spaces_num, list3,c, int(list3)*8+c))
        a += 1
        c += 1
        spaces_num -= 1
        sleep(1)

magic_tree()
