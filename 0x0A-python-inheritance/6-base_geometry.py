#!/usr/bin/python3
"""class inheritor project"""


class BaseGeometry(object):
    """an empty class"""

    def area(self):
        """area method for the class BaseGeometry
          and not data computation"""
        raise Exception("area() is not implemented")
