from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://postgres:boba1234@localhost/postgres')

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.drop_all(engine)