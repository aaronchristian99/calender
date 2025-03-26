from sqlalchemy import Column, Integer, ForeignKey
from database import Base, db_session


class CollaboratedEvent(Base):
    __tablename__ = 'collaborated_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    @classmethod
    def create(cls, data):
        newUser = CollaboratedEvent(
            event_id=int(data['event_id']),
            user_id=data['user_id']
        )
        db_session.add(newUser)

    @classmethod
    def delete(cls, data):
        deleteUser = db_session.query(cls).filter_by(event_id=data['event_id'], user_id=data['user_id']).first()
        db_session.delete(deleteUser)


    @classmethod
    def delete_by_event(cls, event_id):
        deleteEvent = db_session.query(cls).filter_by(event_id=event_id).all()

        for event in deleteEvent:
            db_session.delete(event)

    @classmethod
    def get_by_event(cls, event_id):
        users = db_session.query(cls).filter_by(event_id=event_id).all()
        return [user.to_dict() for user in users]

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'user_id': self.user_id,
        }