from flask import Flask, request
from Controllers.EventController import EventController
from Controllers.LoginController import LoginController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

event_controller = EventController()
login_controller = LoginController()

@app.route('/api/event/create', methods=['POST'])
def create_event():
    data = request.form.to_dict()
    if 'file' in request.files:
        data['file'] = request.files['file']
    return event_controller.createEvent(data)

@app.route('/api/event/update/<int:event_id>', methods=['POST'])
def update_event(event_id):
    data = request.json
    data['id'] = event_id
    return event_controller.updateEvent(data)

@app.route('/api/event/delete/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    return event_controller.deleteEvent(event_id)

@app.route('/api/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    return event_controller.getEventById(event_id)

@app.route('/api/events', methods=['GET'])
def get_events():
    return event_controller.getEvents()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    return login_controller.login(data)

@app.route('/api/logout', methods=['GET'])
def logout():
    return login_controller.logout()

@app.route('/api/user/create', methods=['POST'])
def create_user():
    data = request.json
    return login_controller.createUser(data)

@app.route('/api/users', methods=['GET'])
def get_users():
    return login_controller.getAllUsers()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
