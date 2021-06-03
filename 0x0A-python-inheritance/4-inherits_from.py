#!/usr/bin/python3


"""
functions:
    inherits_from
"""


def inherits_from(obj, a_class):
    """
    this function validate if is a subclass and
    Args:
        obj: any
        a_class: any
    return:True or False
    """
    return issubclass(type(obj), a_class)
