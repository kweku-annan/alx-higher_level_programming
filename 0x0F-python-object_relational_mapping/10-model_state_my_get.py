#!/usr/bin/python3
"""Prints the State object with the name passed as
argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv[1:]

    username = args[0]
    password = args[1]
    db_name = args[2]
    state_name = args[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, db_name
            ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == state_name).all()
    if len(result) == 0:
        print("Not found")
    else:
        for i in result:
            print(i.id)
