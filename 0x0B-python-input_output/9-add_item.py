#!/usr/bin/python3
"""Module to add all"""


import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


myList = []
if os.path.exists("add_item.json"):
    myList = load_from_json_file("add_item.json")
save_to_json_file(myList + sys.argv[1:], "add_item.json")
