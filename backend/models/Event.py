from sqlalchemy import Column, Integer, String, DateTime, Text
from models import Base
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
        newEvent = Event(title=event.title, description=event.description, location=event.location, time=event.time, created_at=datetime.datetime.utcnow(), updated_at=datetime.datetime.utcnow())
        db.session.add(event)
        db.session.commit()

        return newEvent

    @classmethod
    def update(cls, event):
        updatedEvent = db.session.query(cls).filter_by(id=event.id).update({
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'time': event.time,
            'updated_at': datetime.datetime.utcnow(),
        })

        return updatedEvent

    @classmethod
    def get(cls):
        events = db.session.query(cls).all()
        return events

    @classmethod
    def delete(cls, eventId):
        deletedEvent = db.session.query(cls).filter_by(id=eventId).update({
            'deleted_at': datetime.datetime.utcnow()
        })

        return deletedEvent