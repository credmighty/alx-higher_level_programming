#!/usr/bin/python3
"""project I/O of 0x0B"""


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string
    """
    import json

    return (json.loads(my_str))
