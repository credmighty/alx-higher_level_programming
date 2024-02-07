#!/usr/bin/python3
"""project I/O of 0x0B"""


class Student:
    """student class creation"""
    def __init__(self, first_name, last_name, age):
        """initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json method to retrieve dictionary repr"""
        return self.__dict__
