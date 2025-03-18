from models.Event import Event
from models.PrivateEvent import PrivateEvent
from models.PublicEvent import PublicEvent


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
        public_event_id = None
        private_event_id = None

        if data.get('type') == 'public':
            public_event_id = PublicEvent.create(event_id)
        elif data.get('type') == 'private':
            private_event_id = PrivateEvent.create(event_id)

        return {
            'id': event_id,
            'public_event_id': public_event_id,
            'private_event_id': private_event_id
        }

    def updateEvent(self, id, data):
        pass

    def deleteEvent(self, id):
        pass