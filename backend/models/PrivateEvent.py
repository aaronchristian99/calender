from sqlalchemy import Column, Integer, ForeignKey
from models import Base
from database_config import getsession

class PrivateEvent(Base):
    __tablename__ = 'private_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        newPrivateEvent = PrivateEvent(
            event_id=event_id
        )
        getsession().add(newPrivateEvent)
        getsession().commit()

        return newPrivateEvent.id