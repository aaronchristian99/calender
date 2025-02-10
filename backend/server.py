import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from Controllers.EventController import EventController


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.eventController = EventController()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if self.path == '/api/event/create':
            response = self.eventController.createEvent(data)
            self.send_json_response(response)
        elif self.path.startswith('/api/event/update/'):
            event_id = self.extract_id(self.path, '/api/event/update/')
            if event_id is None:
                self.send_error(400, "Invalid ID")
                return

            response = self.eventController.updateEvent(event_id, data)
            self.send_json_response(response)
        elif self.path.startswith('/api/event/delete/'):
            event_id = self.extract_id(self.path, '/api/event/delete/')
            if event_id is None:
                self.send_error(400, "Invalid ID")
                return

            response = self.eventController.deleteEvent(event_id)
            self.send_json_response(response)
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        if self.path == '/api/event/get':
            response = self.eventController.getEvents()
            self.send_json_response(response)
        elif self.path.startswith('/api/event/get/'):
            event_id = self.extract_id(self.path, '/api/event/get/')
            if event_id is None:
                self.send_error(400, "Invalid ID")
                return

            response = self.eventController.getEventById(event_id)
            self.send_json_response(response)
        else:
            self.send_error(404, "Not Found")

    def send_json_response(self, response):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    @staticmethod
    def extract_id(path, prefix):
        """ Extracts an ID from the given path if it's correctly formatted. """
        try:
            event_id = path[len(prefix):]  # Remove the prefix from the path
            return int(event_id) if event_id.isdigit() else None
        except ValueError:
            return None

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()