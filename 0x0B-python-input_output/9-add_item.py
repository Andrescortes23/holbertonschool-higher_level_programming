#!/usr/bin/python3
"""Module to add all arguments to python list and saved in file as json"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
lista = []
try:
    lista = load_from_json_file("add_item.json")
except FileNotFoundError:
    lista = []
lista += argv[1:]
save_to_json_file(lista, "add_item.json")
