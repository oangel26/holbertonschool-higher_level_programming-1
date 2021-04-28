#!/usr/bin/python3
for i in range(1, 90):
    first = i // 10
    second = i % 10
    if first == second:
        continue
    if i > 9 and (first - second) > 0:
        continue
    print("{}{}".format(first, second), end='')
    if i != 89:
        print(', ', end='')
print('')
