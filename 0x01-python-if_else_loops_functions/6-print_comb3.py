#!/usr/bin/python3

for i range(1, 99):
	first = i / 10
	second = i % 10
	if first == second:
		continue
	if i > 9 and first - second:
		continue
	print(first, second)
	if i != 89:
		print(', ')
print('')
