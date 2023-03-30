#!/usr/bin/python3
def pascal_triangle(n):
    """ Defines a function for the representation of pascal Triangle

    Args:
        n = size of triangle

    Returns:
        Pascal triangle
    """
    if n == 0:
        return []

    my_list = []

    for i in range(1, n + 1):
        new = []
        for j in range(i):
            if j == i - 1 or j == 0:
                tmp = 1
            else:
                tmp = my_list[i - 2][j - 1] + my_list[i - 2][j]
            new.append(tmp)
        my_list.append(new)
    return my_list
