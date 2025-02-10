from Event import Event
from datetime import datetime

DATE_DELIMITER = '/'

__events = []
__user_id = '0' # basically the username


def parseTime(time:str):
    time = time.split(DATE_DELIMITER)
    time = [int(t) for t in time]
    time = tuple(time)
    year, month, day, hour, minute = time
    time = datetime(year, month, day, hour, minute)
    return time

# adds event to event list. owner id is the temoprary solution to auth and perms
# is_public and owner_id should no be used until public events are added
# time should be formatted in decending order from year to minute separated by DATE_DELIMITER (eg 2025/02/10/1/54)
def addEvent(title: str, description: str, location: str, time: str, is_public: bool=False, owner_id:str=__user_id) -> bool:
    try:
        new_event = Event(title, description, location, parseTime(time), is_public, owner_id)
        __events.append(new_event)
        return True
    except:
        print("Error when adding event")
        return False

def findEvent(event: Event):
    for index, e in enumerate(__events):
        if e is event:
            return index
        else:
            raise KeyError.add_note("Event not found")

def deleteEvent(event: Event):
    index = findEvent(event)
    __events.pop(index)

def editEvent(event: Event, new_title: str=None, new_description: str=None, new_location: str=None, new_time: str=None, new_visibility: bool=None):
    try:
        if new_title:
            event.setTitle(new_title)
        if new_description:
            event.setDescription(new_description)
        if new_location:
            event.setLocation(new_location)
        if new_time:
            event.setTime(parseTime(new_time))
        if new_visibility:
            event.setVisibility(new_visibility)
    except:
        print("Error editing event")

def getEvent(index: int):
    return __events[index]

def getEvents():
    return __events[:] # duplicates the list so you cant change the order of the stored one

addEvent("", "", "", "2000/1/1/1/1")