#!/usr/bin/python3
"""script that lists all of MySQL"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset='utf8')
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for rows in cur.fetchall():
        if rows[1] == argv[4]:
            print(rows)

    cur.close()
    db.close()
