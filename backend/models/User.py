from sqlalchemy import Column, Integer, String, DateTime
from config.database import Base, db_session
import datetime
import bcrypt

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create(cls, user):
        hashedPassword = bcrypt.hashpw(user.get('password').encode(), bcrypt.gensalt()).decode()
        newUser = User(
            first_name=user.get('firstName'),
            last_name=user.get('lastName'),
            username=user.get('username'),
            password=hashedPassword,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        db_session.add(newUser)
        return newUser.id

    @classmethod
    def update(cls, user):
        hashedPassword = bcrypt.hashpw(user.get('password').encode(), bcrypt.gensalt()).decode()
        updatedUser = db_session.query(cls).filter_by(id=user.id).update({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': hashedPassword,
            'updated_at': datetime.datetime.utcnow(),
        })
        return updatedUser.id

    @classmethod
    def get_all(cls):
        users = db_session.query(cls).all()
        return [cls.to_dict(user) for user in users]

    @classmethod
    def get_by_username(cls, username):
        user = db_session.query(cls).filter_by(username = username).first()
        return cls.to_dict(user)

    @classmethod
    def delete(cls, user_id):
        deletedUser = db_session.query(cls).filter_by(id=user_id).update({
            'deleted_at': datetime.datetime.utcnow()
        })
        return deletedUser.id

    @classmethod
    def to_dict(cls, user):
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            'deleted_at': user.deleted_at.isoformat() if user.deleted_at else None
        }