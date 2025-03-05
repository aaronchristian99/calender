from models.User import User
import bcrypt

class LoginController:
    def __init__(self):
        pass

    def login(self, username, password):
        user = User.getByUsername(username)

        if not user:
            return {
                'success': False,
                'message': 'User not found'
            }

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            return {
                'success': True,
                'message': 'Login successful',
                'user_id': user.id
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