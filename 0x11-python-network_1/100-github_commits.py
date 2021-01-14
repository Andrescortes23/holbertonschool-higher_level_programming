#!/usr/bin/python3
"""
Commits in Github repo
"""

import requests
from sys import argv

repo = argv[1]
user = argv[2]
resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                    .format(repo, user))
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
