from main import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(20), nullable=False)
    event_description = db.Column(db.String(160), nullable=True)
