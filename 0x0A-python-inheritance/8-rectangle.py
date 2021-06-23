#!/usr/bin/python3
"""
Rectangle module

Classes:
    Rectangle (BaseGeometry)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    this class is a base of Geometry
    """

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('heigth', height)
        self.__width = width
        self.__heigth = height
