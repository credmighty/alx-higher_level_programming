#!/usr/bin/python3
"""class inheritor project"""


def add_attribute(obj, at, value):
    """a function that adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, at, value)
