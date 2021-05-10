#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    print('{} {}:'.format(length - 1, 'arguments' if length > 2 else 'argument' ))
    for i in range(1, length):
        print("{0}: {1}".format(i, sys.argv[i]))

