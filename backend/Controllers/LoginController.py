from models.User import User
import bcrypt

class LoginController:
    def __init__(self):
        pass

    def createUser(self, data):
        user_id = User.create(data)
        return user_id

    def login(self, data):
        user = User.get_by_username(data.get('username'))

        if not user:
            return {
                'success': False,
                'message': 'User not found'
            }

        if bcrypt.checkpw(data.get('password').encode(), user.get('password').encode()):
            return {
                'success': True,
                'message': 'Login successful',
                'user': user
            }
        else:
            return {
                'success': False,
                'message': 'Incorrect username or password'
            }

    def logout(self):
        return {
            'success': True,
            'message': 'Logout successful'
        }