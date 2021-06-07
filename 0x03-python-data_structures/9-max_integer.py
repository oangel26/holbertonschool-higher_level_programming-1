#!/usr/bin/python3


def max_integer(my_list=[]):
    greatest = None

    if not my_list:
        return None

    for i in my_list:
        if greatest is None or i > greatest:
            greatest = i

    return greatest
