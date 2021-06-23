#!/usr/bin/python3

""" locked module """


class LockedClass:
    """
    Locked class
    Args:

    Attr:
        first_name : str
    """
    @property
    def first_name(self):
        """ first name getter """
        return(self.__first_name)

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    def __setattr__(self, name: str, value) -> None:
        if name != 'first_name':
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, name))

        value = value
