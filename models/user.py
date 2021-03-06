from werkzeug.security import generate_password_hash, check_password_hash
from main import db, auth
from models import event


class User(db.Model):
    username = db.Column(db.String(20), nullable=False, primary_key=True)
    fullname = db.Column(db.String(128))
    creator = db.relationship("Event")
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, nullable=False)
    reservations = db.relationship(event.Event,
                        secondary=event.event_rsvps)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return None
    else:
        return user.check_password(password)
