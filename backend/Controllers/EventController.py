from models.Event import Event

class EventController:
    def __init__(self):
        pass

    def getEvents(self):
        events = Event.get()
        return {'events': events}

    def getEventById(self, id):
        event = Event.get(id)

    def createEvent(self, data):
        event_id = Event.create(data)
        return {'id': event_id}

    def updateEvent(self, id, data):
        pass

    def deleteEvent(self, id):
        pass