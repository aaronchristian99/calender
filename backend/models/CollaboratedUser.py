from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from models import Base
from database_config import getsession


class CollaboratedUser(Base):
    __tablename__ = 'collaborated_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    @classmethod
    def create(cls, data):
        session = getsession()

        try:
            newUser = CollaboratedUser(
                event_id=data['event_id'],
                user_id=data['user_id']
            )
            session.add(newUser)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete(cls, data):
        session = getsession()

        try:
            deleteUser = session.query(cls).filter_by(event_id=data['event_id'], user_id=data['user_id']).first()
            session.delete(deleteUser)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete_by_event(cls, event_id):
        session = getsession()

        try:
            deleteEvent = session.query(cls).filter_by(event_id=event_id).all()
            session.delete(deleteEvent)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()