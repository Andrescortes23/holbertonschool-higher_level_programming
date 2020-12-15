#!/usr/bin/python3
"""Prints all City objects from the database"""
if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).order_by(City.id).all()
    print(cities)
    for city, state in cities:
        if (state.id == city.state_id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
