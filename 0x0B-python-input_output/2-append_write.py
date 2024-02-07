#!/usr/bin/python3
"""project I/O of 0x0B"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added"""

    with open(filename, 'a', encoding='utf-8') as w_file:
        file_content = w_file.write(text)
    return file_content
