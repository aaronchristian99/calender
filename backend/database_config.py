from os import getenv
from sqlalchemy import create_engine

# Database URL
DATABASE_URL = getenv("DB_URL")

# Creating database engine
engine = create_engine(DATABASE_URL, echo=True)
