#!/usr/bin/python3
"""Script that lists all State objects from the database"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    for state in Session().query(State).order_by(State.id).all():    
        print("{}: {}".format(state.id, state.name))
    Session().close()
