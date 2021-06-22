#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    ''' get only the difference or either'''
    return set_1 | set_2 & set_2 | set_1
