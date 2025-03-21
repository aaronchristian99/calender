from models.User import User
from session_manager.SessionManager import SessionManager
import bcrypt


class LoginController:
    def __init__(self):
        pass

    def createUser(self, data):
        try:
            user_id = User.create(data)
            return { 'user_id': user_id }
        except Exception as e:
            return { 'error': f'Cannot create user: {str(e)}' }

    def login(self, data):
        try:
            user = User.get_by_username(data.get('username'))

            if not user:
                raise Exception('User not found')

            if bcrypt.checkpw(data.get('password').encode(), user.get('password').encode()):
                SessionManager.add('session_id', str(hash(user.get('username'))))
                SessionManager.add('user', user)
                return {
                    'success': True,
                    'message': 'Login successful',
                    'user': user
                }
        except Exception as e:
            return { 'error': f'Cannot login: {str(e)}' }

    def logout(self):
        try:
            SessionManager.remove('session_id')
            SessionManager.remove('user')
            return {
                'success': True,
                'message': 'Logout successful'
            }
        except Exception as e:
            return { 'error': f'Cannot logout: {str(e)}' }