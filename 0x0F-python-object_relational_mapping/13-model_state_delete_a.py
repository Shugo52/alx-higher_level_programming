#!/usr/bin/python3
""" Delete states with 'a' in name"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Connect to mysqldb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Begin a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to load all State instances that have a in their name and delete
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)

    # End and commit session
    session.commit()
