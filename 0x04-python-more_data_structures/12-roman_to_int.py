#!/usr/bin/python3


def roman_to_int(roman_string):
    ''' convert roman letter in num '''
    roman_nums = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    if roman_string is None or type(roman_string) is not str:
        return total

    for idx, letter in enumerate(roman_string):
        if idx < len(roman_string) - 1 \
                and roman_nums[roman_string[idx + 1]] > roman_nums[letter]:
            total += roman_nums[letter]
        else:
            total -= roman_nums[letter]

    return abs(total)
