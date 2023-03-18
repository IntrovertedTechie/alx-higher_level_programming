#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    if len(sys.argv) == 4:
        USER = sys.argv[1]
        PASSWORD = sys.argv[2]
        DB_NAME = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(USER, PASSWORD, DB_NAME),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_state.cities.append(new_city)

        session.add(new_state)
        session.add(new_city)
        session.commit()

        session.close()

