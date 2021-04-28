#!/usr/bin/python3
def uppercase(str):
    for i, c in enumerate(str):
        ascii = ord(c)
        if ascii >= 97 and ascii <= 122:
            c = chr(ascii - 32)
        print(c, end='')
    print('')
