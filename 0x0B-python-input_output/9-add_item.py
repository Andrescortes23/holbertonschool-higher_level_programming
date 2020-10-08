#!/usr/bin/python3
"""Module to add all arguments to python list and saved in file as json"""


import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    lista = load_from_json_file("add_item.json")
except:
    lista = []
for a in range(1, len(sys.argv)):
    lista.append(sys.argv[a])
save_to_json_file(lista, "add_item.json")
