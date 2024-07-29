#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter 'a'
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

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, db_name
            ),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states_to_delete = session.query(State).filter(
            State.name.contains('a')).all()
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    except e:
        session.rollback()
        raise
    finally:
        session.close()
