#!/usr/bin/python3
import sys

if __name__ == '__main__':
    print('{} arguments'.format(len(sys.argv) - 1))

    for i, a in enumerate(sys.argv):
        if i == 0:
            continue
        print("{0}: {1}".format(i, a))
