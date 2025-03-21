from sqlalchemy import Column, Integer, ForeignKey
from models import Base
from database_config import getsession

class PrivateEvent(Base):
    __tablename__ = 'private_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    @classmethod
    def create(cls, event_id):
        session = getsession()

        try:
            newPrivateEvent = PrivateEvent(
                event_id=event_id
            )
            session.add(newPrivateEvent)
            session.commit()

            return newPrivateEvent.id
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    @staticmethod
    def is_private(event_id):
        session = getsession()

        try:
            private_event_id = session.query(PrivateEvent).filter_by(event_id=event_id).first()

            return private_event_id if private_event_id is not None else False
        except Exception as e:
            raise
        finally:
            session.close()