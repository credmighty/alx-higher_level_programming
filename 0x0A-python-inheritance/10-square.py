#!/usr/bin/python3
"""class inheritor project"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Sqaure inherits from Rectanle (9-rectangle.py)"""
    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area methood to be implemented"""
        return self.__size * self.__size
