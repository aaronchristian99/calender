from models.User import User
from session_manager import SessionManager
import bcrypt


class LoginController:
    def __init__(self):
        self.session_manager = SessionManager()

    """
        Create a user
        @param data: The user data
        @return: userId
    """
    def createUser(self, data):
        try:
            user_id = User.create(data)
            return { 'user_id': user_id }
        except Exception as e:
            return { 'error': f'Cannot create user: {str(e)}' }

    """
        Logging in the user
        @param data: The user data
        @return: success, message and user
    """
    def login(self, data):
        try:
            user = User.get_by_username(data.get('username'))

            if not user:
                raise Exception('User not found')

            if bcrypt.checkpw(data.get('password').encode(), user.get('password').encode()):
                self.session_manager.add('session_id', str(hash(user.get('username'))))
                self.session_manager.add('user', user)
                return {
                    'success': True,
                    'message': 'Login successful',
                    'user': user
                }
        except Exception as e:
            return { 'error': f'Cannot login: {str(e)}' }

    """
        logs out the user
        @return: success, message and user
    """
    def logout(self):
        try:
            self.session_manager.remove('session_id')
            self.session_manager.remove('user')
            return {
                'success': True,
                'message': 'Logout successful'
            }
        except Exception as e:
            return { 'error': f'Cannot logout: {str(e)}' }

    """
        Retrieves all users
        @return: users
    """
    def getAllUsers(self):
        try:
            users = User.get_all()
            return { 'users': users }
        except Exception as e:
            return { 'error': f'Cannot get users: {str(e)}' }