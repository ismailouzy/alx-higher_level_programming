#!/usr/bin/python3
"""
    script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
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
    new = session.query(State, City).join(City).order_by(asc(City.id))
    for i, j in new.all():
        print("{}: ({:d}) {}".format(i.name, j.id, j.name))
    session.commit()
    session.close()
