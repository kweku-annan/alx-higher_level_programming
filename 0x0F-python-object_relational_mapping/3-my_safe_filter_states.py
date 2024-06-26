#!/usr/bin/python3
"""Takes an argument and displays all values in
   the states table of hbtn_0e_0_usa where name matches
   the argument
"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def all_states(host, user, passwd, db_name, state_name):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("""
        SELECT *
        FROM states
        WHERE name = %s
        COLLATE utf8mb4_0900_as_cs
        ORDER BY states.id ASC
    """, (state_name,))
    result = cur.fetchall()
    return (result)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]
    state_name = ARGS[3]

    states = all_states('localhost', username, password, db_name, state_name)
    for row in states:
        print(row)
