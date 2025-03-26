from sqlalchemy import Column, Integer, ForeignKey
from database import Base, db_session

class PublicEvent(Base):
    __tablename__ = 'public_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        newPublicEvent = PublicEvent(
            event_id=event_id
        )
        db_session.add(newPublicEvent)
        return newPublicEvent.id

    
    @staticmethod
    def is_public(event_id):
        public_event = db_session.query(PublicEvent).filter_by(event_id=event_id).first()
        return public_event.id if public_event is not None else False

    @staticmethod
    def delete(event_id):
        public_event = db_session.query(PublicEvent).filter_by(event_id=event_id).first()
        db_session.delete(public_event)