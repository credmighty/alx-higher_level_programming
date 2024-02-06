#!/usr/bin/python3
"""class inheritor project"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """method for initialization child class rectangle"""
        super().integer_validator('width', width)
        self.__with = width
        super().integer_validator('height', height)
        self.__height = height
