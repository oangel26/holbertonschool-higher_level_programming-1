#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print(''.format(None))
        return
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=' ')
        print('')
