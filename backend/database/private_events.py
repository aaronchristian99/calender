from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

from backend.database_config import engine

Base = declarative_base()

class Events(Base):
    __tablename__ = 'private_events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))