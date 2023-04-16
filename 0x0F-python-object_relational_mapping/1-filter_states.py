#!/usr/bin/python3
"""
script lists all states with name starting with capital N
args; username, password and databasename
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]")
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    rows = cur.fetchall()
    for state in rows:
        if state[1][0] == "N":
            print (state)
