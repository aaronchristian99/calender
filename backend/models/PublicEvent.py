from sqlalchemy import Column, Integer, ForeignKey
from models import Base
from database_config import getsession

class PublicEvent(Base):
    __tablename__ = 'public_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        newPublicEvent = PublicEvent(
            event_id=event_id
        )
        getsession().add(newPublicEvent)
        getsession().commit()

        return newPublicEvent.id