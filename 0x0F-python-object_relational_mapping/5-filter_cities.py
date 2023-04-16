#!/usr/bin/python3
"""
takes in the name of a state as an argument 
and lists all cities of that state, using the database 
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    rows = cur.fetchall()
    print(", ".join([city[2]
                     for city in rows
                     if city[4] == sys.argv[4]]))
