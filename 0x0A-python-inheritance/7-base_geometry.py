#!/usr/bin/python3
"""
Geometry module

Classes:
    BaseGeometry
"""


class BaseGeometry:
    """
    this class is a base of Geometry
    """

    def area(self):
        """
        blueprint method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator
        Args:
            name: string
            value: int
        Raise:
            - TypeError is not int
            - ValueError if value is less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
