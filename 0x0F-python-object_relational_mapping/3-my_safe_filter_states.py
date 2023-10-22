#!/usr/bin/python3
"""All states listed from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306, charset="utf8" 
                         )
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
