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
        session = getsession()

        try:
            hashedPassword = bcrypt.hashpw(user.get('password').encode(), bcrypt.gensalt()).decode()
            newUser = User(
                first_name=user.get('firstName'),
                last_name=user.get('lastName'),
                username=user.get('username'),
                password=hashedPassword,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            session.add(newUser)
            session.commit()

            return newUser.id
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def update(cls, user):
        session = getsession()

        try:
            hashedPassword = bcrypt.hashpw(user.get('password').encode(), bcrypt.gensalt()).decode()
            updatedUser = session.query(cls).filter_by(id=user.id).update({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'password': hashedPassword,
                'updated_at': datetime.datetime.utcnow(),
            })
            getsession().commit()
            return updatedUser.id
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def get_by_username(cls, username):
        session = getsession()

        try:
            user = session.query(cls).filter_by(username = username).first()
            return cls.to_dict(user)
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete(cls, user_id):
        session = getsession()

        try:
            deletedUser = session.query(cls).filter_by(id=user_id).update({
                'deleted_at': datetime.datetime.utcnow()
            })
            session.commit()
            return deletedUser.id
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

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