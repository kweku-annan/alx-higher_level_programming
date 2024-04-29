#!/usr/bin/python3
"""Lists all states objects from the database
hbtn_0e_6_usa using SQLAlchemy (ORM)
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":

    args = sys.argv[1:]

    username = args[0]
    password = args[1]
    db_name = args[2]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if (session.query(State).count() == 0):
        print()
    else:
        result = session.query(State).order_by(State.id).first()
        if result is None:
            print()
        else:
            print("{}: {}".format(result.id, result.name))
