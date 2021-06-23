#!/usr/bin/python3


def best_score(a_dictionary):
    ''' find max value in dictionary '''
    max_value = -1
    max_key = None

    if not a_dictionary:
        return
    for k, v in a_dictionary.items():
        if max_value is None or v > max_value:
            max_value = v
            max_key = k

    if max_value == -1:
        return
    return max_key
