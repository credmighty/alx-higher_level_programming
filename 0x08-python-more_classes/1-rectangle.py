#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    def width(self):
        return self.__width

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.height = value

    def width(self):
        return self.__width
