#!/usr/bin/python3
"""Indentation module"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sym = text.replace('.', '.\n\n')
    sym = sym.replace('?', '?\n\n')
    sym = sym.replace(':', ':\n\n')
    sym1 = sym.split('\n')
    for line in range(len(sym1)):
        print("{}".format(sym1[line].strip()),
              end=("" if (line == (len(period1) - 1)) else '\n'))
