#!/usr/bin/python3
"""select all states module"""

import sys
import MySQLdb

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # create cursor
    cur = db.cursor()

    # execute query
    cur.execute("SELECT * FROM states")

    # obtain query results
    items = cur.fetchall()

    # print query result
    for i in items:
        print(i)

    # close cursor and database
    cur.close()
    db.close()
