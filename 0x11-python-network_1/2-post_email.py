#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')

    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
