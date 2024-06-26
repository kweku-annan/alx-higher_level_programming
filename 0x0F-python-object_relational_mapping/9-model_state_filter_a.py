#!/usr/bin/python3
"""Lists all State objects that contain the letter a."""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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

    result = session.query(State)\
                    .filter(State.name.like("%a%"))\
                    .order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
