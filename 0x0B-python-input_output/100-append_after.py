#!/usr/bin/python3

"""project I/O for 0x0B"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    text = ""
    with open(filename, encoding='utf-8') as f:
        for lines in f:
            text += lines
            if search_string in lines:
                text += new_string

    with open(filename, "w", encoding='utf-8') as wr:
        wr.write(text)
