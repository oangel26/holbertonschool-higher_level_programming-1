#!/usr/bin/python3
"""this is a rectangle class"""


class Rectangle:
    """Rectangle class

       class attributes
       number_of_instances :int
       Args:
       width: int
       height int
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.print_symbol = '#'
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """int: width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """return area"""
        return self.width * self.height

    def perimeter(self):
        """compute perimeter """
        if (self.width == 0 or self.height == 0):
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """string format"""
        text = ''

        if self.height == 0 or self.width == 0:
            return text

        for i in range(self.height):
            for j in range(self.width):

                if type(self.print_symbol) is str:
                    text = text + self.print_symbol
                else:
                    text = text + str(self.print_symbol)
            if i + 1 != self.height:
                text += '\n'
        return text

    def __repr__(self):
        """repr: """
        text = "Rectangle({}, {})"
        text = text.format(self.width, self.height)
        return text

    def __del__(self):
        """delete event"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
