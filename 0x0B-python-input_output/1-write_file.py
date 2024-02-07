#!/usr/bin/python3
"""project I/O of 0x0B"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as w_file:
        file_content = w_file.write(text)
        return file_content
