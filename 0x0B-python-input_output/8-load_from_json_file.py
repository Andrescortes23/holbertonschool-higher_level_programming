#!/usr/bin/python3
"""Module to create object from json file"""
import json


def load_from_json_file(filename):
    """Function to creat object"""
    with open(filename, encoding='UTF8') as myFile:
        return json.load(myFile)
