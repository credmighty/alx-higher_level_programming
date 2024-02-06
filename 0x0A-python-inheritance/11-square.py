#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """class Square that inherits from Rectangle (9-rectangle.py):"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area methood to be implemented"""
        return self.__size * self.__size

    def __str__(self):
        """magic str return, the square desc: [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size)
