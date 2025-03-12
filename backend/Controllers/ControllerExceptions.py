# Exceptions for the controller classes
#==============================================================================
# Login exceptions

# database holds no user with the given username
class UserNotFoundException(Exception):
    def __init__(self, username):
        self.message = f'User with username {username} does not exist'

# username provided is already in the database
class DuplicateUserException(Exception):
    def __init__(self, username):
        self.message = f'User with username {username} already exists'

# username provided is not allowed
class InvalidUsernameException(Exception):
    def __init__(self, username):
        self.message = f'Username {username} is not allowed'

# password provided does not match the password in the database
class IncorrectPasswordException(Exception):
    def __init__(self):
        self.message = 'Incorrect username or password' # username mentioned in case the wrong username is entered but still exists
#==============================================================================
# Event exceptions

# event with the given id does not exist
class EventNotFoundException(Exception):
    def __init__(self, id):
        self.message = f"Event '{id}' does not exist"

# event could not be created due to something
class EventCreationException(Exception):
    def __init__(self):
        self.message = 'Event could not be created'

# event could not be updated due to something (same stuff as creating)
class EventUpdateException(Exception):
    def __init__(self, id):
        self.message = f"Event '{id}' could not be updated" 