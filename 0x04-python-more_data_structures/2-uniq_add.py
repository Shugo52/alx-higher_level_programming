#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum([my_list[i] if my_list[i]
           not in my_list[:i] else 0 for i in range(len(my_list))])
