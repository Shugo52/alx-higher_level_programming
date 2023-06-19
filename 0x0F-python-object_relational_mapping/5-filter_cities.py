#!/usr/bin/python3
"""cities by state module"""

import sys
import MySQLdb

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # get cursor
    cur = db.cursor()

    # execute query
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                states.id=cities.state_id WHERE states.name LIKE %s",
                (sys.argv[4], ))

    # obtain query results
    items = cur.fetchall()

    # print result
    item_list = [i[0] for i in items]
    print(*item_list, sep=', ')

    # close db
    cur.close()
    db.close()
