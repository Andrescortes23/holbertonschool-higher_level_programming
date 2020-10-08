#!/usr/bin/python3
"""Module to add all"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

myList = []
try:
    myList = load_from_json_file("add_item.json")
except:
    myList = []
myList += sys.argv[1:]
save_to_json_file(myList, "add_item.json")
