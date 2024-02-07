#!/usr/bin/python3
"""project I/O for 0x0B"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a 'JSON file'"""
    with open(filename, 'r', encoding='utf-8') as f:
        f_read = f.read()
    return json.loads(f_read)
