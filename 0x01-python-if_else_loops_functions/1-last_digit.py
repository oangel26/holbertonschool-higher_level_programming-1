#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10)
if number < 0:
    last_digit = last_digit * -1
if number < 0:
    last_digit = last_digit * -1
if last_digit == 0:
    msg = "and is 0"
elif last_digit > 5:
    msg = "and is greater than 5"
elif last_digit < 6 and not 0:
    msg = "and is less than 6 and not 0"
print("Last digit of %d is %d %s" % (number, last_digit, msg))

