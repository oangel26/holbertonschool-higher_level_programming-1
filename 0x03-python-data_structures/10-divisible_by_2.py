#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result = []

    if len(my_list) == 0:
        return []

    for i in my_list:
        result.append(i % 2 == 0)

    return result
