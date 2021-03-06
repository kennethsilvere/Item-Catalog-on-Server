from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('postgresql://vagrant:vagrant@localhost/restaurantmenuwithusers')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

pepperoni = MenuItem()