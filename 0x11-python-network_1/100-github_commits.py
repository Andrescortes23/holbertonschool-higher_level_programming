#!/usr/bin/python3
"""
Commits in Github repo
"""

import requests
from sys import argv

repo = argv[1]
user = argv[2]
resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                    .format(user, repo))
resp = resp.json()
iterat = 0
while iterat < 10:
    print("{}: {}".format(resp[iterat].get('sha'),
                          resp[iterat].get('commit').get('author').get('name')))
    iterat += 1
