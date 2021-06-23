#!/usr/bin/python3


def roman_to_int(roman_string):
    ''' convert roman letter in num '''
    roman_nums = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    if roman_string is None or type(roman_string) is not str:
        return total

    for letter in roman_string:
        total += roman_nums[letter]

    return total
