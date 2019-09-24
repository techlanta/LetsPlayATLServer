from main import app, db
from models.event import Event
from flask import request, jsonify

@app.route("/event", methods=['POST'])
def events():
    content = request.json #only works if content type is application/json
    name = content["name"]
    event = Event(name=name)
    db.session.add(event)
    db.session.commit()

    return jsonify({"status": "created", "event": {"name": name, "id": event.id}})
