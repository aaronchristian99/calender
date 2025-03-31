from models.Event import Event
from models.PrivateEvent import PrivateEvent
from models.PublicEvent import PublicEvent
from models.CollaboratedEvent import CollaboratedEvent
from collections import Counter
from flask import jsonify, session, flash
from config.database import db_session
import os
import PyPDF2
import traceback


class EventController:
    def __init__(self):
        pass

    def getEvents(self):
        try:
            user_id = session.get('user_id')
            events = Event.get_all()
            filtered_events = []

            for event in events:
                users = [user['user_id'] for user in CollaboratedEvent.get_by_event(event['id'])]

                if (user_id in users or
                    event['type'] == 'public' or
                    (event['type'] == 'private' and event['created_by'] == user_id)):
                    filtered_events.append(event)

            return jsonify({
                'events': list(events)
            }), 200
        except Exception as e:
            return jsonify({
                'error': f'Error getting events: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    def getEventById(self, id):
        try:
            event = Event.get_by_id(id)
            users = CollaboratedEvent.get_by_event(id)
            tagCount, tags = self.getTags(id)
            return jsonify({
                'event': event,
                'tagCount': tagCount,
                'tags': tags,
                'users': users
            }), 200
        except Exception as e:
            return jsonify({
                'error': f'Error getting events: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    def createEvent(self, data):
        try:
            event_id = Event.create(data)
            public_event_id = None
            private_event_id = None
            index = 0

            if data.get('type') == 'public':
                public_event_id = PublicEvent.create(event_id)
            elif data.get('type') == 'private':
                private_event_id = PrivateEvent.create(event_id)

            while f'collaborated_users[{index}][key]' in data:
                CollaboratedEvent.create({
                    'user_id': data.get(f"collaborated_users[{index}][key]"),
                    'event_id': event_id
                })
                index += 1

            if 'file' in data:
                file = data.get('file')
                filename = f'event_{event_id}.pdf'
                self.isDirectoryExists()
                filepath = os.path.join('storage/app/files', filename)
                with open(filepath, 'wb') as f:
                    f.write(file.read())

            event = Event.get_by_id(event_id)

            db_session.commit()

            return jsonify({
                'event': event,
                'message': 'Event created successfully'
            }), 200
        except Exception as e:
            db_session.rollback()
            return jsonify({
                'error': f'Error creating event: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    def updateEvent(self, data):
        try:
            Event.update(data)
            public_event_id = None
            private_event_id = None
            index = 0

            if data.get('type') == 'public':
                if PrivateEvent.is_private(data['id']):
                    PrivateEvent.delete(data['id'])
                if not PublicEvent.is_public(data['id']):
                    public_event_id = PublicEvent.create(data['id'])
            elif data.get('type') == 'private':
                if PublicEvent.is_public(data['id']):
                    PublicEvent.delete(data['id'])
                if not PrivateEvent.is_private(data['id']):
                    private_event_id = PrivateEvent.create(data['id'])

            CollaboratedEvent.delete_by_event(data['id'])

            while f'collaborated_users[{index}][key]' in data:
                CollaboratedEvent.create({
                    'user_id': data.get(f"collaborated_users[{index}][key]"),
                    'event_id': data['id']
                })

            event = Event.get_by_id(data['id'])
            users = CollaboratedEvent.get_by_event(data['id'])

            db_session.commit()

            return jsonify({
                'event': event,
                'users': users,
                'message': 'Event updated successfully'
            }, 200)
        except Exception as e:
            db_session.rollback()
            return jsonify({
                'error': f'Error updating events: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

    def deleteEvent(self, id):
        try:
            event_id = Event.delete(id)
            db_session.commit()
            return jsonify({
                'id': event_id,
                'message': 'Event deleted successfully'
            }), 200
        except Exception as e:
            db_session.rollback()
            return jsonify({
                'error': f'Error deleting events: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500

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
        except FileNotFoundError:
            # Return an empty array for tags if the file is not found
            return 0, []
        except Exception as e:
            raise