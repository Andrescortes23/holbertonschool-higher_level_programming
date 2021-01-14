#!/usr/bin/python3
"""
Commits in Github repo
"""

import requests
from sys import argv

repo = argv[2]
user = argv[1]
resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                    .format(user, repo))
resp = resp.json()
for a in resp:
    for b in a:
        if b == 'sha':
            sha = a[b]
        if b == 'commit':
            for c in a[b]:
                if c == 'author':
                    for d in a[b][c]:
                        if d == 'name':
                            authname = a[b][c][d]
                            iterat = 0
while iterat < 10:
    print("{}: {}".format(sha, authname))
    iterat += 1
