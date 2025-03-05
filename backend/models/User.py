from sqlalchemy import Column, Integer, String, DateTime
from models import Base
from database_config import getsession
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
        hasedPassword = bcrypt.hashpw(user.get('password'), bcrypt.gensalt()).decode()
        newUser = User(
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            username=user.get('username'),
            password=hasedPassword,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        getsession().add(newUser)
        getsession().commit()

        return newUser.id

    @classmethod
    def update(cls, user):
        hasedPassword = bcrypt.hashpw(user.get('password'), bcrypt.gensalt()).decode()
        updatedUser = getsession().query(cls).filter_by(id=user.id).update({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': hasedPassword,
            'updated_at': datetime.datetime.utcnow(),
        })
        getsession().commit()

        return updatedUser.id

    @classmethod
    def getByUsername(cls, username):
        user = getsession().query(cls).filter_by(username=username).first()
        return cls.to_dict(user)

    @classmethod
    def delete(cls, user_id):
        deletedUser = getsession().query(cls).filter_by(id=user_id).update({
            'deleted_at': datetime.datetime.utcnow()
        })
        getsession().commit()

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