#!/usr/bin/python3
"""Fetch cities by state"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


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

    result = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id).all()
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
