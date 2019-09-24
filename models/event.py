
from main import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    longitude = db.Column(db.Float,)
    latitude = db.Column(db.Float,)
    ongoing = db.Column(db.Boolean,)
    startDate = db.Column(db.DateTime,)
