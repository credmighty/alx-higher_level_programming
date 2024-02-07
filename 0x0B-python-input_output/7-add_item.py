#!/usr/bin/python3
"""project I/O for 0x0B"""

from sys import argv
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
itemList = []
if os.path.exists(filename):
    itemList = load_json_file(filename)
save_to_json_file(itemList + argv[1:], filename)
