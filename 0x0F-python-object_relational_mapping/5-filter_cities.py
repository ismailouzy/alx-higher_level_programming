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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC", [sys.argv[4]])
    rows = cur.fetchall()

    for i in rows:
        j.append(i[1])
    print(", ".join(j))

    cur.close()
    con.close()
