from main import app, db, auth
from models.event import Event
from models.user import User
from flask import request, jsonify
import dateutil.parser
from models import sdg, event


@app.route("/event", methods=['POST'])
@auth.login_required
def create_event():
    content = request.json #only works if content type is application/json
    assert "name" in content
    name = content["name"]



    event = Event(name=name)
    event.fromDict(content)
    event.parent_id = auth.username()
    db.session.add(event)
    db.session.commit()

    return jsonify({"status": "created", "event": event.toDict()})

@app.route("/event", methods=["DELETE"])
@auth.login_required
def remove_event():
    content = request.json
    assert "id" in content
    user = User.query.filter_by(username=auth.username()).first()
    event = Event.query.filter_by(id=content["id"]).first()
    if event is None:
        return "event not found!"
    deleted = False
    if user.is_admin:
        db.session.delete(event)
        deleted = True
    else:
        if event.parent_id == auth.username():
            db.session.delete(event)
            deleted = True

    db.session.commit()
    return jsonify({"success": deleted})

@app.route("/event/tag/<tag>", methods=["GET"])
def get_event_by_tags(tag):
    event_tag_pairs = event.Tag.query.filter_by(tag=tag).limit(100)
    toReturn = []
    for event_tag_pair in event_tag_pairs:
        toReturn.append(event_tag_pair.event.toDict())
    return jsonify(toReturn)

@app.route("/event/tag", methods=['POST'])
@auth.login_required
def tag_event():
    content = request.json #only works if content type is application/json
    assert "id" in content
    assert "tag" in content
    # event_id = content["id"]
    tag = content["tag"]


    event = Event.query.filter_by(id=content["id"]).first()
    # return jsonify(event)
    if event is None:
        return "no such event!"
    if event.parent_id != auth.username():
        return "not allowed"
    event.add_tag(tag)

    return jsonify({"status": "created", "event": event.toDict()})

@app.route("/event/tag", methods=['DELETE'])
@auth.login_required
def delete_tag_event():
    content = request.json #only works if content type is application/json
    assert "id" in content
    assert "tag" in content
    # event_id = content["id"]
    tag = content["tag"]
    tag = event.Tag.query.filter_by(event_id=content["id"], tag=tag).first()




    # return jsonify(event)
    if tag is None:
        return "no such tag"
    if tag.event.parent_id != auth.username():
        return "not allowed"
    db.session.delete(tag)
    db.session.commit()

    return jsonify({"status": "removed", "event": tag.event.toDict()})

@app.route("/event/rsvp/", methods=["GET"])
@auth.login_required
def get_RSVP_by_user():
    user_obj = User.query.filter_by(username=auth.username()).first()
    if user_obj is None:
        return "no such user!"
    events = user_obj.reservations
    allEventDicts = []
    for foundEvent in events:
        allEventDicts.append(foundEvent.toDict())
    return jsonify(allEventDicts)

@app.route("/event/rsvp", methods=['POST'])
@auth.login_required
def rsvp():
    content = request.json #only works if content type is application/json
    assert "id" in content
    foundEvent = Event.query.filter_by(id=content["id"]).first()
    if foundEvent is None:
        return "no such event!"
    user_obj = User.query.filter_by(username=auth.username()).first()
    user_obj.reservations.append(foundEvent)
    db.session.add(user_obj)
    db.session.commit()
    return jsonify({"status": "created rsvp", "username": auth.username(), "event": foundEvent.toDict()})

@app.route("/event/id", methods=['POST'])
def get_event_by_id():
    content = request.json
    assert "id" in content
    event = Event.query.filter_by(id=content["id"]).first()
    if event is not None:
        return jsonify(event.toDict())
    else:
        return "event not found"

@app.route("/event", methods=['GET'])
def get_all_events():
    events = Event.query.limit(300).all()
    toReturn = []
    for event in events:
        eventDict = event.toDict()
        toReturn.append(eventDict)
    return jsonify(toReturn)

@app.route("/event/latLong", methods=["POST"])
def get_events_nearby():
    content = request.json
    assert "latitude" in content
    assert "longitude" in content
    if "max_mile" in content:
        max_mile = float(content["max_mile"])
    else:
        max_mile = 5
    delta = max_mile / 69.9 / 2 #difference in latitude or longitude


    events = Event.query.filter(
        (Event.latitude < float(content["latitude"]) + delta)).filter( \
        (Event.latitude > float(content["latitude"]) - delta)).filter( \
        (Event.longitude < float(content["longitude"]) + delta)).filter( \
        (Event.longitude > float(content["longitude"]) - delta)
        )
    toReturn = []
    for event_result in events:
        toReturn.append(event_result.toDict())
    return jsonify(toReturn)

@app.route("/event/sdg", methods=["GET"])
def get_all_SDGs():
    sdgs = sdg.ALL_SDG
    # content = request.json
    # if "id" in content:
    #     return jsonify(sdg.get_sdg(int(content["id"])))
    # else:
    return jsonify([sdg.serialize() for sdg in sdgs])

@app.route("/event", methods=["PUT"])
@auth.login_required
def update_event():
    content = request.json
    assert "id" in content
    assert "name" in content
    id = content["id"]
    id = int(id)
    oldEvent = Event.query.filter_by(id=id).first()
    oldEvent.fromDict(content)
    db.session.add(oldEvent)
    db.session.commit()

    return jsonify({"status": "updated", "event": oldEvent.toDict()})
