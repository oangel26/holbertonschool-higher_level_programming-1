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

    def __init__(self, size=0):
        """Constructor
        Args:
            size (int): size of square `size`.
        Raises:
        TypeError: The ``size`` size must be an integer.
        ValueError: ``size`` must be >= 0.

        """
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

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
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
