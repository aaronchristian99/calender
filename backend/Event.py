from datetime import datetime

class Event:
    def __init__(self, title: str, description: str, location: str, time: datetime, visibility: bool, owner_id:str):
        self.__title = title
        self.__description = description
        self.__location = location
        self.__time = time
        self.__visibility = visibility #True = public, False = private
        self.__owner_id = owner_id
       
    def getTitle(self):
        return self.__title
    
    def setTitle(self, new_title):
        self.__title = new_title
    
    def getDescription(self):
        return self.__description
    
    def setDescription(self, new_description):
        self.__description = new_description

    def getLocation(self):
        return self.__location
    
    def setLocation(self, new_location):
        self.__location = new_location
    
    def getTime(self):
        return self.__time
    
    def setTime(self, new_time):
        self.__time = new_time
    
    def getVisibility(self):
        return self.__visibility

    def setVisibility(self, new_visibility):
        self.__visibility = new_visibility

    def isOwner(self, user_id: str) -> bool:
        return user_id == self.__owner_id
    
    def __repr__(self):
        return f"The event name is '{self.__title}', It is a {"public" if self.__is_public else "private"} event, and will take place on {self.__time}."

