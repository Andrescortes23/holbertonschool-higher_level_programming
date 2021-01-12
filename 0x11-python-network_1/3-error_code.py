#!/usr/bin/python3
"""
Send a request to the URL and displays the body of the response
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as therror:
        print("Error code: {}".format(therror.code))
