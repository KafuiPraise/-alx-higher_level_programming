#!/usr/bin/python3
""" Prints State object with the name passed as argument from the database
"""

import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    match = sys.argv[4]
    attr = session.query(State).filter_by(name=match).first()
    if attr is not None:
        print(str(attr.id))
    else:
        print("Not found")
    session.close()
