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

    # Add new State instance
    new_state = State(name="Louisiana")
    session.add(new_state)

    # query to load first State instance that matches new state name
    state = session.query(State).filter_by(name='Louisiana').first()

    # Print id of new state
    print(state.id)

    # End and commit session
    session.commit()
