from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from models import Base
from models.PrivateEvent import PrivateEvent
from models.PublicEvent import PublicEvent
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
    created_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
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
            raise
        finally:
            session.close()

    @classmethod
    def update(cls, event):
        session = getsession()

        try:
            updatedEvent = session.query(cls).filter_by(id=event.id).update({
                'title': event.title,
                'description': event.description,
                'location': event.location,
                'start_at': event.start_at,
                'end_at': event.end_at,
                'updated_at': datetime.datetime.utcnow(),
            })
            return updatedEvent
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = getsession()

        try:
            events = (session.query(cls, PrivateEvent.id.label('private_event_id'), PublicEvent.id.label('public_event_id'))
                            .outerjoin(PrivateEvent, Event.id == PrivateEvent.event_id)
                            .outerjoin(PublicEvent, Event.id == PublicEvent.event_id)
                            .filter(Event.deleted_at.is_(None))
                            .all())

            if events is None:
                raise Exception('No events found.')

            return [cls.to_dict(event) for event in events]
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def get_by_id(cls, event_id):
        session = getsession()

        try:
            event = (session.query(cls, PrivateEvent.id.label('private_event_id'), PublicEvent.id.label('public_event_id'))
                            .outerjoin(PrivateEvent, Event.id == PrivateEvent.event_id)
                            .outerjoin(PublicEvent, Event.id == PublicEvent.event_id)
                            .filter(Event.id == event_id, Event.deleted_at.is_(None))
                            .first())

            if event is None:
                raise Exception('Event not found')

            return cls.to_dict(event)
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete(cls, event_id):
        session = getsession()

        try:
            deletedEvent = getsession().query(cls).filter_by(id=event_id).update({
                'deleted_at': datetime.datetime.utcnow()
            })
            return deletedEvent
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def to_dict(cls, event):
        event_type = None

        if event[1] is not None:
            event_type = 'private'
        elif event[2] is not None:
            event_type = 'public'

        return {
            'id': event[0].id,
            'title': event[0].title,
            'description': event[0].description,
            'location': event[0].location,
            'start_at': event[0].start_at.isoformat() if event[0].start_at else None,
            'end_at': event[0].end_at.isoformat() if event[0].end_at else None,
            'type': event_type,
            'created_by': event[0].created_by,
            'created_at': event[0].created_at.isoformat(),
            'updated_at': event[0].updated_at.isoformat(),
            'deleted_at': event[0].deleted_at.isoformat() if event[0].deleted_at else None
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
