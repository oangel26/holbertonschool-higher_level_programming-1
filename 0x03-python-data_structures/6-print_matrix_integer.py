#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    greatest = None
    for row in matrix:
        max_n = max(matrix)
        if greatest is None or max_n > greatest:
            greatest = max_n
    return greatest
