from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import sessionmaker
from models import Base
from database_config import getsession
import datetime

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(255), nullable=False)
    time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create(cls, event):
        newEvent = Event(
            title=event.get('title'),
            description=event.get('description'),
            location=event.get('location'),
            time=event.get('date'),
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        getsession().add(newEvent)
        getsession().commit()

        return newEvent.id

    @classmethod
    def update(cls, event):
        updatedEvent = getsession().query(cls).filter_by(id=event.id).update({
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'time': event.time,
            'updated_at': datetime.datetime.utcnow(),
        })

        return updatedEvent

    @classmethod
    def get(cls):
        events = getsession().query(cls).all()
        return [cls.to_dict(event) for event in events]

    @classmethod
    def get_by_id(cls, event_id):
        event = getsession().query(cls).filter_by(id=event_id)
        return cls.to_dict(event)

    @classmethod
    def delete(cls, event_id):
        deletedEvent = getsession().query(cls).filter_by(id=event_id).update({
            'deleted_at': datetime.datetime.utcnow()
        })

        return deletedEvent

    @classmethod
    def to_dict(cls, event):
        return {
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'time': event.time.isoformat() if event.time else None,
            'created_at': event.created_at.isoformat(),
            'updated_at': event.updated_at.isoformat(),
            'deleted_at': event.deleted_at.isoformat() if event.deleted_at else None
        }
