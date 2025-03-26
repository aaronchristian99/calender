from flask import jsonify, session
from models.User import User
import bcrypt
import traceback


class LoginController:
    def __init__(self):
        pass

    """
        Create a user
        @param data: The user data
        @return: userId
    """
    def createUser(self, data):
        try:
            user_id = User.create(data)
            return jsonify({ 'user_id': user_id }), 200
        except Exception as e:
            return jsonify({
                'error': f'Cannot create user: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

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
                session['session_id'] = str(hash(user.get('username')))
                session['user_id'] = user.get('id')
                session.permanent = True
                return jsonify({
                    'success': True,
                    'message': 'Login successful',
                    'user': user
                }), 200
        except Exception as e:
            return jsonify({
                'error': f'Cannot login: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    """
        logs out the user
        @return: success, message and user
    """
    def logout(self):
        try:
            session.pop('session_id', None)
            session.pop('user', None)
            return jsonify({
                'success': True,
                'message': 'Logout successful'
            }), 200
        except Exception as e:
            return jsonify({
                'error': f'Cannot logout: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    """
        Retrieves all users
        @return: users
    """
    def getAllUsers(self):
        try:
            users = User.get_all()
            return jsonify({ 'users': users }), 200
        except Exception as e:
            return jsonify({
                'error': f'Cannot get users: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500