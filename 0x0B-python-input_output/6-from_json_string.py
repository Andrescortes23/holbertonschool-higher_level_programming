#!/usr/bin/python3
"""Module to get object represented by json"""
import json


def from_json_string(my_str):
    """Function to return object by json str"""
    return json.loads(my_str)
