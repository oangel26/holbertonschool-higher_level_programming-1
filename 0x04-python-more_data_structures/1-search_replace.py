#!/usr/bin/python3


def search_replace(my_list, search, replace):
    ''' search and replace function '''
    result = []
    for item in my_list:
        if item == search:
            result.append(replace)
        else:
            result.append(item)
    return result
