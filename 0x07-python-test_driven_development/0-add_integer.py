#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """Return the integer addition of a and b
     Float arguments are typecasted to int before addition is performed
     Raises:
         TypeError: {messages}
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
