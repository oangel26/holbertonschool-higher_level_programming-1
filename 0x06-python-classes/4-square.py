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

    def __init__(self, value=0):
        """Constructor
        Args:
            value (int): value of square `value`.
        Raises:
        TypeError: The ``value`` value must be an integer.
        ValueError: ``value`` must be >= 0.

        """
        self.size = value

    def area(self):
        """Compute the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
