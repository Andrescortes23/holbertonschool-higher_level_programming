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
    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(id=6, name='Louisiana')
    session.add(new)
    session.commit()
    states = session.query(State).order_by(State.id.desc()).first()
    print(states.id)
    session.close()
