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

    # id of event to edit and data to change it to
    def updateEvent(self, id, data):
       data.id = id
       Event.update(data)

    def deleteEvent(self, id):
        Event.delete(id)