#!/usr/bin/python3


def weight_average(my_list=[]):
    ''' calculate average weight '''
    length = len(my_list)
    total_weight = 0
    denominator = 0
    if length == 0:
        return 0

    for t in my_list:
        denominator += t[0] * t[1]
        total_weight += t[1]

    return denominator / total_weight
