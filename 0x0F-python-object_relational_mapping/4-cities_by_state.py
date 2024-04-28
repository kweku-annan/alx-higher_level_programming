#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def list_cities(username, passwd, db_name):
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=passwd, db=db_name
        )
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
    """)
    result = cur.fetchall()
    return (result)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]

    cities = list_cities(username, password, db_name)
    for row in cities:
        print(row)
