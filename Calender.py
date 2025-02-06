from datetime import datetime

class Event:
    def __init__(self, name, date: datetime, visibility):
        self.__name = name
        self.__visibility = visibility
        self.__date = date
       
    def returnName(self):
        return self.__name
    def returnVis(self):
        return self.__visibility 
    def returnDate(self):
        return self.__date
    def __repr__(self):
        return f"The event name is '{self.__name}', It is a {"public" if self.__visibility else "private"} event, and will take place on {self.__date}."

