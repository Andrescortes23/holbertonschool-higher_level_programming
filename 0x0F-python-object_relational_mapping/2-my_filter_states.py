#!/usr/bin/python3
"""Display a state that matches with input"""


import MySQLdb
from sys import argv
if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    thestate = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if thestate in row:
            print ("{}".format(row))
    cur.close()
    db.close()
