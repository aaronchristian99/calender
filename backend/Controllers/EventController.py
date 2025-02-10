from models import Event

class EventController:
    def __init__(self):
        pass

    def getEvents(self):
        pass

    def getEventById(self, id):
        pass

    def createEvent(self, data):
        eventData = {
            'title': data.get('title'),
            'description': data.get('description'),
            'location': data.get('location'),
            'time': data.get('time')
        }
        event = Event.create(eventData)
        return event

    def updateEvent(self, id, data):
        pass

    def deleteEvent(self, id):
        pass