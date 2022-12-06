#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        tmp = 0
        for index, item in enumerate(my_list):
            if my_list[index] > tmp:
                tmp = my_list[index]
            else:
                continue
        return tmp
    else:
        return None
