#!/usr/bin/python3
"""project I/O of 0x0B"""
import json

to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation
    """
    json_data = to_json_string(my_obj)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_data)
