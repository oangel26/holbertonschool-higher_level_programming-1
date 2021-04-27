#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg = ""
last_digit = abs(number) % 10

# 1. Tomar ultimo digito con valor absoluto
# 2.
# 2.1 mirar si el ultimo digito es 0
# 2.2 mirar mayor 5
# 2.3 mirar is menor a 6 y no es 0

if last_digit == 0:
    msg = "and is 0"
elif last_digit > 5:
    msg = "and is greater than 5"
else:
    msg = "and is less than 6 and not 0"
if number < 0:
    last_digit = last_digit * -1

print("Last digit of %d is %d %s" % (number, last_digit, msg))
