#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) + len(tuple_b) < 4:
        return 0

    return tuple(tuple_a[0] + tuple_b[0], tuple_b[1], tuple_b[1])
