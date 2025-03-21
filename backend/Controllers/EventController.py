from models.Event import Event
from models.PrivateEvent import PrivateEvent
from models.PublicEvent import PublicEvent
from session_manager import SessionManager


class EventController:
    def __init__(self):
        pass

    def getEvents(self):
        user = SessionManager.get('user')
        try:
            events = filter(lambda event: event.type == 'public' or (event.type == 'private' and event.created_by == user.get('id')), Event.get_all())
            return {'events': events}
        except Exception as e:
            return { 'error': f'Error getting events: {str(e)}'}

    def getEventById(self, id):
        try:
            event = Event.get_by_id(id)
            return {'event': event}
        except Exception as e:
            return { 'error': f'Error getting events: {str(e)}'}

    def createEvent(self, data):
        try:
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
                'private_event_id': private_event_id,
                'message': 'Event created successfully'
            }
        except Exception as e:
            return { 'error': f'Error getting events: {str(e)}'}

    # id of event to edit and data to change it to
    def updateEvent(self, data):
        try:
            event_id = Event.update(data)
            public_event_id = None
            private_event_id = None

            if data.get('type') == 'public':
                public_event_id = PublicEvent.create(event_id)
            elif data.get('type') == 'private':
                private_event_id = PrivateEvent.create(event_id)

            return {
                'id': event_id,
                'public_event_id': public_event_id,
                'private_event_id': private_event_id,
                'message': 'Event updated successfully'
            }
        except Exception as e:
            return { 'error': f'Error updating events: {str(e)}'}

    def deleteEvent(self, id):
        try:
            event_id = Event.delete(id)
            return {'id': event_id, 'message': 'Event deleted successfully'}
        except Exception as e:
            return { 'error': f'Error deleting events: {str(e)}'}