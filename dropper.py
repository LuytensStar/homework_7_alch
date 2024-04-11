from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from db_engine import Session, engine

session = Session()

Base = declarative_base()

Base.metadata.drop_all(engine)