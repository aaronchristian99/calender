from sqlalchemy import Column, Integer, ForeignKey
from models import Base
from database_config import getsession

class PublicEvent(Base):
    __tablename__ = 'public_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        session = getsession()

        try:
            newPublicEvent = PublicEvent(
                event_id=event_id
            )
            session.add(newPublicEvent)
            session.commit()
            return newPublicEvent.id
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    @staticmethod
    def is_public(event_id):
        session = getsession()

        try:
            public_event_id = session.query(PublicEvent).filter_by(event_id=event_id).first()
            return public_event_id if public_event_id is not None else False
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()