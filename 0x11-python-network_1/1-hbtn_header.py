#!/usr/bin/python3
"""Send a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""


from urllib import request
import sys

with request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
