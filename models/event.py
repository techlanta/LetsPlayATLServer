from main import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    parent_id = db.Column(db.String(20), db.ForeignKey('user.username'))
    longitude = db.Column(db.Float,)
    latitude = db.Column(db.Float,)
    ongoing = db.Column(db.Boolean,)
    startDate = db.Column(db.DateTime,)
