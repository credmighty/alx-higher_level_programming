#!/usr/bin/python3
"""class inheritor project"""


class MyList(list):
    """this class inherits from list"""

    def print_sorted(self):
        """method that sorts and print list"""
        print(sorted(self))
