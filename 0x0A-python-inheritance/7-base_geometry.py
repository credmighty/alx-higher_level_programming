#!/usr/bin/python3
"""class inheritor project"""


class BaseGeometry(object):
    """ class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """area method of the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates values"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
