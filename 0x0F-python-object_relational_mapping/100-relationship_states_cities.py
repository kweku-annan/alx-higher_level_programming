#!/usr/bin/python3
"""Creates the State "California" with the City"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    username = args[0]
    passwrd = args[1]
    db_name = args[2]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, passwrd, db_name
            ),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    city1 = City(name="San Francisco", state=california)
    session.add(california)
    session.commit()
