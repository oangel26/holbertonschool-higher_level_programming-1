#!/usr/bin/python3
"""created class Square that inherits that Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        """Call the super class with id, x, y, call with __init__ ,  or class parent"""
        super().__init__(size, size, x, y, id)
        """asignation"""
        self.size = size

    """getter and setter public, its width and height have the same values"""
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        self.__width = value
        self.__height = value

    """overloading"""
    def __str__(self, **kwargs):
        return  ("[Square] ({}) {}/{} - {}".format
            (self.id, self.x, self.y, self.size))

    """adding method public"""
    def update(self, *args, **kwargs):
        if len(args):
            """args non-kwargs"""
            for iter_arg, arg in enumerate(args):
                if iter_arg == 0:
                    self.id = arg
                elif iter_arg == 1:
                    self.size = arg
                elif iter_arg == 2:
                    self.x = arg
                elif iter_arg == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    """by adding the public method, that returns the dictionary"""
    def to_dictionary(self):
        vars = ['id', 'size', 'x', 'y']
        dict = {}
        for i in range(len(vars)):
            dict.update({vars[i]: getattr(self, vars[i])})
        return dict



if __name__ == "__main__":
    from base import Base
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))