#!/usr/bin/python3
""" Change the name of a state with id=2"""

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

    # query to load first State instance that matches id=2
    state = session.query(State).filter_by(id=2).first()

    # Change name of state
    state.name = "New Mexico"

    # End and commit session
    session.commit()
