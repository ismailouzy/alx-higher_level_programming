#!/usr/bin/python3
"""
    script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    stmt = session.query(State).\
        filter(State.name == sys.argv[4]).order_by(State.id).all()
    if stmt:
        print("{}".format(stmt[0].id))
    else:
        print("Not found")
    session.close()
