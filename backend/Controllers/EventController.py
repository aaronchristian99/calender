from models.Event import Event
from models.PrivateEvent import PrivateEvent
from models.PublicEvent import PublicEvent
from models.CollaboratedUser import CollaboratedUser
from session_manager import SessionManager
from collections import Counter
import os
import PyPDF2


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
            tagCount, tags = self.getTags(id)
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

            if len(data.get('collaborated_users')) > 0:
                for id in data.get('collaborated_users'):
                    CollaboratedUser.create({
                        'user_id': id,
                        'event_id': event_id
                    })

            if data.get('file'):
                filename = f'event_{event_id}.pdf'
                self.isDirectoryExists()
                filepath = os.path.join('storage/app/files', filename)
                with open(filepath, 'wb') as f:
                    f.write(data.get('file').file.read())

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

            CollaboratedUser.delete_by_event(event_id)

            if len(data.get('collaborated_users')) > 0:
                for id in data.get('collaborated_users'):
                    CollaboratedUser.create({
                        'user_id': id,
                        'event_id': event_id
                    })

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

    def isDirectoryExists(self):
        if not os.path.exists('storage/app/files'):
            os.makedirs('storage/app/files')

    def getTags(self, id):
        stop_words = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
                      "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to",
                      "was", "were", "will", "with"}
        filepath = f'storage/app/files/event_{id}.pdf'

        try:
            with open(filepath, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                words = text.lower().split()
                filtered_words = [word for word in words if word not in stop_words]
                word_count = len(filtered_words)
                word_frequencies = Counter(filtered_words)
                repeated_words = [word for word, count in word_frequencies.items() if count > 1]

                return word_count, repeated_words
        except Exception as e:
            raise