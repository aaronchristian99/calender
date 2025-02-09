from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class PublicEvent(Base):
    __tablename__ = 'public_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))