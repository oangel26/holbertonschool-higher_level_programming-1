#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    ''' multiply all items in a list with number'''
    return list(map(lambda x: x * number, my_list))
