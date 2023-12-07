from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///DBHorizonte.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()