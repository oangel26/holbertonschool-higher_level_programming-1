#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print('0 arguments.')
        exit(0)
    msg = 'arguments' if length > 2 else 'argument'
    print('{} {}:'.format(length - 1, msg))
    for i in range(1, length):
        print("{0}: {1}".format(i, sys.argv[i]))
