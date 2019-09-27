from main import app, db, auth
from models.event import Event
from flask import request, jsonify


@app.route("/event", methods=['POST'])
@auth.login_required
def create_event():
    content = request.json #only works if content type is application/json
    assert "name" in content
    assert "user_id" in content
    name = content["name"]
    event = Event(name=name)
    db.session.add(event)
    db.session.commit()

    return jsonify({"status": "created", "event": {"name": name, "id": event.id}})
