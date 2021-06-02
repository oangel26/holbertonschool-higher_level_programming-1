#!/usr/bin/python3

"""
module
classes
    MyList
"""


class MyList(list):
    """
    class MyList
    """

    def print_sorted(self):
        """
            this function copy list and print sorted values
            Args:
                self: Mylist
        """
        copied = self.copy()
        copied.sort()
        print(copied)
        return copied
