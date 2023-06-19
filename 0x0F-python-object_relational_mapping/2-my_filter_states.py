#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # get cursor
    cur = db.cursor()

    # execute query
    cur.execute("SELECT * FROM states WHERE name LIKE\
                BINARY '{}' ORDER BY states.id".format(sys.argv[4]))

    # obtain query results
    items = cur.fetchall()

    # print result
    for i in items:
        print(i)

    # close db
    cur.close()
    db.close()
