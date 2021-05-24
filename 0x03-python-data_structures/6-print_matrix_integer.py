#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    greatest = None
    if len(matrix) == 1:
        print('')
        return
    for row in matrix:
        max_n = max(row)
        if greatest is None or max_n > greatest:
            greatest = max_n
    print("{}".format(greatest))
