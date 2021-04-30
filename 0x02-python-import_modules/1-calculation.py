#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

if __name__ == '__main__':
	a = 10
	b = 5
	print("{} + {} = {}".format(a, b, add(10, 5)))
	print("{} - {} = {}".format(a, b, sub(10, 5)))
	print("{} * {} = {}".format(a, b, mul(10, 5)))
	print("{} / {} = {}".format(a, b, div(10, 5)))
