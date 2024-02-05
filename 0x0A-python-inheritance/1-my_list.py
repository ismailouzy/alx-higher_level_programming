#!/usr/bin/python3
"""sub class Mylist

"""


class MyList(list):
    """ a class MyList that inherits from list"""

    def __innit__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
