#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sum_n = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            sum_n += int(sys.argv[i])
    print(sum_n)
