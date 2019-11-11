from main import db
from models import sdg, event
import dateutil.parser



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128),)

    parent_id = db.Column(db.String(20), db.ForeignKey('user.username'))
    longitude = db.Column(db.Float,)
    latitude = db.Column(db.Float,)
    ongoing = db.Column(db.Boolean,)
    startDate = db.Column(db.DateTime,)
    endDate = db.Column(db.DateTime,)
    sdg = db.relationship("SDG",
                    secondary=sdg.sdg_to_events)


    def toDict(self):
        eventDict = {}
        eventDict["name"] = self.name
        eventDict["description"] = self.description
        if (self.startDate is not None and self.endDate is not None):
            eventDict["startDate"] = self.startDate.isoformat()
            eventDict["endDate"] = self.endDate.isoformat()
        else:
            eventDict["startDate"] = None
            eventDict["endDate"] = None

        if self.latitude is not None and self.longitude is not None:
            eventDict["latitude"] = self.latitude
            eventDict["longitude"] = self.longitude
        eventDict["id"] = self.id
        sdg_events_rows = db.session.query(sdg.sdg_to_events).filter_by(event_id=self.id).limit(100)
        if sdg_events_rows.count() > 0:
            eventDict["sdg"] = []
            for sdg_event_row in sdg_events_rows:
                eventDict["sdg"].append(sdg.get_sdg(sdg_event_row.sdg_id))
        tag_event_rows = Tag.query.filter_by(event_id=self.id).limit(100)
        if tag_event_rows.count() > 0:
            eventDict["tags"] = []
            for tag_event_row in tag_event_rows:
                eventDict["tags"].append(tag_event_row.tag)
        return eventDict

    def remove_all_sdg(self):
        '''
        Run this when doing an update!
        '''
        self.sdg = []
        db.session.commit()

    def add_sdg(self, sdg_id):
        sdg_obj = sdg.SDG.query.filter_by(id=sdg_id).first()
        # self.ad
        self.sdg.append(sdg_obj)
        db.session.add(self)
        db.session.commit()



    def add_tag(self, tag):
        tag = Tag(event_id=self.id, tag=tag)
        db.session.add(tag)
        db.session.commit()

    def fromDict(self, content):
        if "name" in content.keys():
            self.name = content["name"]
        if "description" in content.keys():
            self.description = content["description"]
        try:
            if "longitude" in content.keys():
                self.longitude = float(content["longitude"])
            if "latitude" in content.keys():
                self.latitude = float(content["latitude"])
        except Exception:
            print("Could not grab latLong", content["longitude"], content["latitude"])
        if "ongoing" in content.keys():
            self.ongoing = content["ongoing"] == True
        else:
            self.ongoing = False
        if "startDate" in content.keys() and content["startDate"] is not None:
            self.startDate = dateutil.parser.parse(content["startDate"])
        if "endDate" in content.keys() and content["endDate"] is not None:
            self.endDate = dateutil.parser.parse(content["endDate"])
        if "sdg" in content.keys() and self.id is not None:
            sdg_event_mappings = content["sdg"]
            self.remove_all_sdg()
            for sdg_event_mapping in sdg_event_mappings:
                self.add_sdg(sdg_event_mapping["id"])

class Tag(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    tag = db.Column(db.String(20), primary_key=True)
    event = db.relationship(Event, backref='event')

# event_tags = db.Table(
#     "event_tags",
#     db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
#     db.Column("tag", db.String(20), primary_key=True)
#     )

event_rsvps = db.Table(
    "event_rsvps",
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    db.Column("username", db.String(20), db.ForeignKey("user.username"), primary_key=True)
    )
