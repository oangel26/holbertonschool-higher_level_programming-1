#!/usr/bin/python3

def best_score(a_dictionary):
    ''' find max value in dictionary '''
    max_value = -1
    for k, v in a_dictionary:
        if v > max_value:
            max_value = v
    return max_value