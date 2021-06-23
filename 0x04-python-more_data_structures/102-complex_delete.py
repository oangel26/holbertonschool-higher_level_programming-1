#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys_to_del = []

    if not a_dictionary:
        return None

    for k, v in a_dictionary.items():
        if v == value:
            keys_to_del.append(k)

    for key in keys_to_del:
        del a_dictionary[key]
    return a_dictionary
