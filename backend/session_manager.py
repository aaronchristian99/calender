
class SessionManager:
    def __init__(self):
        # Global session storage (temporary, in-memory)
        self.sessions = {}

    """
    Add key value pair to sessions
    @param key: The key of key-value pair
    @value: The value of key-value pair
    """
    def add(self, key, value):
        self.sessions[key] = value

    """
    Retrieves value of session key
    @param key: The key.
    @returns value: The value associated with the key.
    """
    def get(self, key):
        return self.sessions.get(key)

    """
    Removes the user from the session.
    @param key: The key.
    @returns None
    """
    def remove(self, key):
        self.sessions.pop(key, None)
