#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
r = []
if os.path.exists(filename):
    r = load(filename)
save(r + argv[1:], filename)
