from main import app, db
from models.event import Event

@app.route("/events", methods=['POST'])
def events():
    event = Event(event_name="Momo's community block party")
    db.session.add(event)
    db.session.commit()
    content = request.json #only works if content type is application/json
    return jsonify(events_c.create(content["name"]))
