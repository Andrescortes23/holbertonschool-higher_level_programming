#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        q = ""
        print("No result")
    else:
        q = sys.argv[1]
        if q.isalpha():
            data = {'q': q}
            resp = requests.post('http://0.0.0.0:5000/search_user', data)
            try:
                resp = resp.json()
                print("[{}] {}".format(resp.get('id'), resp.get('name')))
            except:
                print("Not a valid JSON")
        else:
            print("No result")
