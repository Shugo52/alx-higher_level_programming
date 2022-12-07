#!/usr/bin/python3
def weight_average(my_list=[]) -> float:
    if my_list:
        product = sum([num[0] * num[1] for num in my_list])
        denominator = sum([num[1] for num in my_list])
        return product / denominator
    else:
        return 0
