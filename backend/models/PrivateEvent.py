from sqlalchemy import Column, Integer, ForeignKey
from database import Base, db_session

class PrivateEvent(Base):
    __tablename__ = 'private_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        newPrivateEvent = PrivateEvent(
            event_id=event_id
        )
        db_session.add(newPrivateEvent)
        return newPrivateEvent.id

    
    @staticmethod
    def is_private(event_id):
        private_event_id = db_session.query(PrivateEvent).filter_by(event_id=event_id).first()
        return private_event_id if private_event_id is not None else False