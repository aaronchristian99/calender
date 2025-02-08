from os import getenv
from sqlalchemy import create_engine

# Loading the environment variables
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")

# Database URL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:3306/{MYSQL_DATABASE}"

# Creating database engine
engine = create_engine(DATABASE_URL, echo=True)
