#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j in matrix[i]:
                print("{:d}".format(j), end="")
                if matrix[i].index(j) != (len(matrix[i]) - 1):
                    print(" ", end="")
            print()
