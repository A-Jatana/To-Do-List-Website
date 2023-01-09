from . import db #basically same thing as import website (if outside of directory)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #one user has many notes thats why foreignkey (one to many)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(300), unique=True)
    password = db.Column(db.String(300))
    first_name = db.Column(db.String(300))
    notes = db.relationship('Note')