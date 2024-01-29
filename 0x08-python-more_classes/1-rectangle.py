#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    def width(self):
        return self.__width

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def height(self):
        return self.__height
