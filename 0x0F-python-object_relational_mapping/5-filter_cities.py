#!/usr/bin/python3
"""Takes the name of a state as an argument and lists
   all cities of that states.
"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def list_cities_by_state(username, password, db_name, state_name):
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=db_name
        )
    cur = db.cursor()
    cur.execute("""
       SELECT cities.name
       FROM cities
       JOIN states
       ON states.id = cities.state_id
       WHERE states.name = %s
    """, (state_name, ))
    result = cur.fetchall()
    return (result)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]
    state_name = ARGS[3]

    cities = list(
        list_cities_by_state(username, password, db_name, state_name)
    )
    if len(cities) <= 0:
        print()
    for i, j in enumerate(cities):
        if i < len(cities) - 1:
            print("{}, ".format(j[0]), end="")
        else:
            print("{}".format(j[0]))
