#!/usr/bin/python3
"""Print the first State object from the database"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    #    if states:
    try:
        thestate = Session().query(State).first()
        print("{}: {}".format(thestate.id, thestate.name))
    except Exception:
        print("Nothing")
    Session().close()
