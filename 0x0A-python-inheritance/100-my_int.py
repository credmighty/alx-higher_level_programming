#!/usr/bin/python3
"""class inheritor project"""


class MyInt(int):
    """MyInt is a subclass of integer class"""

    def __init__(self, inp):
        """initialization"""
        self.inp = inp

    def __eq__(value1, value2):
        """inverts == operation for !="""
        return value1.inp != value2

    def __ne__(value1, value2):
        """inverts == operation for !="""
        return value1.inp == value2
