#!/usr/bin/python3
"""function to print square module"""


def print_square(size):
    """print a square made of #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    s = '#' * size
    for x in range(size):
        print(s)
