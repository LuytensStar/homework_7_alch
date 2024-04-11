from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:boba1234@localhost/postgres')

Session = sessionmaker(bind=engine)