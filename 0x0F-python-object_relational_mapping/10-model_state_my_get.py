#!/usr/bin/python3
""" Fetch from state"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    # Connect to mysqldb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Begin a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to load State instance that matches a pattern
    state = session.query(State).filter(State.name.like(f"%{sys.argv[4]}%"))
    try:
        print(state[0].id)
    except IndexError:
        print("Not found")
