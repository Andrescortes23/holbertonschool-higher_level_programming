#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    tosearch = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == tosearch).first()
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()
