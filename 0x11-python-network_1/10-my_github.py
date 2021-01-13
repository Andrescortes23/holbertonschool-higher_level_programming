#!/usr/bin/python3
"""
Get id from my GitHub profile
"""


import requests
from sys import argv

if len(argv) > 1:
    prof = (argv[1], argv[2])
    try:
        response = requests.get('https://api.github.com/user', auth=prof)
        print(response.json().get('id'))
    except:
        print("None")
