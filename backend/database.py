from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# Database URL
DATABASE_URL = getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")

# Creating database engine
engine = create_engine(DATABASE_URL, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models.User import User
    from models.Event import Event
    from models.PublicEvent import PublicEvent
    from models.PrivateEvent import PrivateEvent
    from models.CollaboratedEvent import CollaboratedEvent
    Base.metadata.create_all(bind=engine)