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

    def __init__(self, size=3):
        """Constructor
        Args:
            size (int): size of square `size`.
        """
        self.__size = size
