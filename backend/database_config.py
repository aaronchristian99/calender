from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")

# Creating database engine
engine = create_engine(DATABASE_URL, echo=True)

# Creating session factory
Session = sessionmaker(bind=engine)
session = Session()

# Return session object
def getsession():
    return session