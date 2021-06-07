#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print('{:s}'.format(''))
        return
    for row in matrix:
        for i,  col in enumerate(row):
            print("{:d}".format(col), end='')
            if i != len(row) - 1:
                print(' ', end='')
        print('')
