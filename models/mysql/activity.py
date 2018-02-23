from models.mysql.init import db
import datetime

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=True)
    sessionId = db.Column(db.String(36),nullable=True)

    userId = db.Column(db.String(12),nullable=True)
    accessToken = db.Column(db.String(40),nullable=True)
    applicationID  = db.Column(db.String(36),nullable=True)
    apiAccessToken = db.Column(db.String(320),nullable=True)

    deviceId = db.Column(db.String(320),nullable=True)

    # intents = db.relationship("Intents", backref=db.backref('activity', lazy=True))
    query = db.Column(db.String(100),nullable=True)
    type = db.Column(db.String(10),nullable=True)

    dialogRequestId = db.Column(db.String(36),nullable=True)
    requestId = db.Column(db.String(34),nullable=True)

    dialogState = db.Column(db.String(10),nullable=True)

    timestamp = db.Column(db.DateTime(),nullable=False,
        default=datetime.datetime.now)

    def __repr__(self):
        return '<Activity %r>' % self.username

class Intents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name