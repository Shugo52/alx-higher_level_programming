#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for i in range(len(matrix)):
        for i in matrix[i]:
            print("{:d}".format(i), end=" ")
        print()
