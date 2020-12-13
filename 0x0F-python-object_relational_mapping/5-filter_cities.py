#!/usr/bin/python3
"""Script that lists all cities from a given state"""


import MySQLdb
from sys import argv
if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    thestate = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities\
    INNER JOIN states ON cities.state_id=states.id\
    WHERE states.name=%(state)s ORDER BY cities.id ASC",
                {'state': thestate})
    rows = cur.fetchall()
    cnt = 0

    for row in rows:
        for city in row:
            if cnt < len(rows) - 1:
                print(city, end=', ')
            elif cnt == len(rows) - 1:
                print(city, end='')
            cnt += 1
    print()
    cur.close()
    db.close()
