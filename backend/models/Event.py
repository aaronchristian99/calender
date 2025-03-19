from sqlalchemy import Column, Integer, String, DateTime, Text
from models import Base
from database_config import getsession
import datetime

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(255), nullable=False)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create(cls, event):
        session = getsession()

        try:
            newEvent = Event(
                title=event.get('title'),
                description=event.get('description'),
                location=event.get('location'),
                start_at=cls.parse_datetime(event.get('start_at')),
                end_at=cls.parse_datetime(event.get('end_at')),
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            session.add(newEvent)
            session.commit()
            return newEvent.id
        except Exception as e:
            session.rollback()
            return 'Error inserting event'

    @classmethod
    def update(cls, event):
        updatedEvent = getsession().query(cls).filter_by(id=event.id).update({
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'start_at': event.start_at,
            'end_at': event.end_at,
            'updated_at': datetime.datetime.utcnow(),
        })

        return updatedEvent

    @classmethod
    def get(cls):
        events = getsession().query(cls).all()
        return [cls.to_dict(event) for event in events]

    @classmethod
    def get_by_id(cls, event_id):
        event = getsession().query(cls).filter_by(id=event_id).first()
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
            'start_at': event.start_at.isoformat() if event.start_at else None,
            'end_at': event.end_at.isoformat() if event.end_at else None,
            'created_at': event.created_at.isoformat(),
            'updated_at': event.updated_at.isoformat(),
            'deleted_at': event.deleted_at.isoformat() if event.deleted_at else None
        }
    

    
    @staticmethod
    def get_description_tags(event_description): #returns a list of tags in the description
        possible_tags = ['work', 'other', 'important', 'urgent', 'fun', 'budget', 'meeting', 'salary', 'party', 'project', 'assignment', 'conference'] # add any new tags here
        tags = {}
        for word in event_description.split(' '):
            for tag in possible_tags:
                if tag in word.lower():
                    tags.append(tag)
        return tags

    @staticmethod
    def parse_datetime(dt_str):
        """ Convert ISO 8601 string to Python datetime object """
        if dt_str:
            return datetime.datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
        return None
