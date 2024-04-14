#!/usr/bin/python3
"""
states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    con = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                          passwd=sys.argv[2], db=sys.argv[3])

    cur = con.cursor()
    cur.execute("""SELECT * FROM states WHERE name like "N%"\
            ORDER BY states.id ASC""")
    rows = cur.fetchall()

    for i in rows:
        print(i)
