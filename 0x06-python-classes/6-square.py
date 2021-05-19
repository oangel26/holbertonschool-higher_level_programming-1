#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square data.

Square class allow all data and methods of the square

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""


class Square:
    """this is the empty class Square
    Args:
    Attributes:
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
            size (int): size of square `size`.
        Raises:
        TypeError: The ``size`` size must be an integer.
        ValueError: ``size`` must be >= 0.
        """
        self.size = size
        self.position = position

    def area(self):
        """Compute the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """ int: size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """ int: position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """print square with #"""

        if self.size == 0:
            print('')
            return

        for _ in range(self.__position[1]):
            print('')
        for _ in range(self.size):
            if self.position[1] == 0:
                print(" " * self.__position[0], end='')
            print('#' * self.size, end='')
            print('')
