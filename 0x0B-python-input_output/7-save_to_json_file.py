#!/usr/bin/python3
"""Method to write a object to a file with json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write object to a file with json representation"""
    with open(filename, 'w', encoding='UTF8') as myFile:
        json.dump(my_obj, myFile)
