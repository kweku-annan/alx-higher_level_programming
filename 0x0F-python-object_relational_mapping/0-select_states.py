#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def all_states(host, user, passwd, db_name):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    result = cur.fetchall()
    return (result)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]

    states = all_states('localhost', username, password, db_name)
    for row in states:
        print(row)
