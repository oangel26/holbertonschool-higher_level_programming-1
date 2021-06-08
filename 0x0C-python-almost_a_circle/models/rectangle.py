#!/usr/bin/python3
"""
    module documentation
    created class that inherits of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class constructor, instance attributes
    Args:
        - width (int)
        - height (int)
        - x (int)
        - y (int)
        - id (int)
    call super class, with id, call with __init__ ,  or class parent
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter and setter for each instance attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """update class Rectangle, add public method, return area value"""
        return self.width * self.height

    def display(self):
        """
        display rectangle with # char
        """
        print('\n' * self.__y, end='')
        for iter_h in range(self.__height):
            print(' ' * self.__x,  end='')
            print("#" * self.__width)

        """update class Rectangle, add public method,
        print # for width and height"""
        if self.width == 0 or self.height == 0:
            print("")

    def __str__(self):
        """Overriding method"""
        text_format = "[Rectangle] ({}) {}/{} - {}/{}"
        return text_format.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """method that assings ags each atri... and update  args and kwargs"""
        if len(args):
            for iter_args, arg in enumerate(args):
                if iter_args == 0:
                    self.id = arg
                elif iter_args == 1:
                    self.__width = arg
                elif iter_args == 2:
                    self.__height = arg
                elif iter_args == 3:
                    self.__x = arg
                elif iter_args == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """update class that returns the dictionary representation of a Rectangle"""
        vars = ['x', 'y', 'id', 'height', 'width']
        dict = {}
        print(self.__dict__)
        for i in range(len(vars)):
            dict.update({vars[i]: getattr(self, vars[i])})
        return dict
