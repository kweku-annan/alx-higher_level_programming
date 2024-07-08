#!/usr/bin/python3
"""Contains the class definition of 'State'"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


""" engine = create_engine(
    "mysql+mysqldb://christassaah:emma%401495@localhost:3306/\
hbtn_0e_6_usa")
"""


class State(Base):
    """Inherits from Base"""
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True,
        nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")


# Base.metadata.create_all(engine)
