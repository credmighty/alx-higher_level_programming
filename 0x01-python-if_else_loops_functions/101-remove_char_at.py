#!/usr/bin/python3
def remove_char_at(str, a):
    """function of copy string without the character at position a"""
    if a < 0:
        return (str)
    return (str[:a] + str[a+1:])
