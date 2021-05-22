#!/usr/bin/python3
"""this is a rectangle class"""


class Rectangle:
    """Rectangle class
       Args:
       width: int
       height int
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        self.__height = value

    @property
    def width(self):
        """int: width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        self.__width = value

#    def __repr__(self):
#        """repr: """
#        return "{'_Rectangle__heigth': {}, '_Rectangle__width': {}}"
#    .format(self.height, self.width)
