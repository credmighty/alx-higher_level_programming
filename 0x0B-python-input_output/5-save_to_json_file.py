#!/usr/bin/python3
"""project I/O of 0x0B"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
