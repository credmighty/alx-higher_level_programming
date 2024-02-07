#!/usr/bin/python3
"""project I/O of 0x0B"""


class Student:
    """student class creation"""
    def __init__(self, first_name, last_name, age):
        """initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json method to retrieve dictionary repr"""
        if attrs is None:
            return self.__dict__
        dict_ = {}
        for values in attrs:
            if hasattr(self, values):
                dict_[values] = getattr(self, values)
        return dict_
