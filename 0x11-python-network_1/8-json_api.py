#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter.
"""


import requests
import sys

if len(sys.argv) < 2:
    q = ""
    print("No result")
else:
    q = sys.argv[1]
    if q.isalpha():
        resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        resp = resp.json()
        print("[{}] {}".format(resp.get('id'), resp.get('name')))
    else:
        print("No result")
