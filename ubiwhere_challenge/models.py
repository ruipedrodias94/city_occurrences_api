from flask_sqlalchemy import SQLAlchemy
from ubiwhere_challenge import db
from flask_login import UserMixin
from datetime import datetime

"""
In this package will be defined the database models
"""

class User(db.Model, UserMixin):

    """
    This class defines the user model

    :param id: (int) id of user, primary key, generated automatically 
    :param username: (string) username
    :param email: (string) email
    :param password: (string) password
    :param occurrences: (Occurrence) occurrences
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    occurrences = db.relationship('Occurrence', backref='user', lazy=True)

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return "<User %r>" % self.username


class Occurrence(db.Model):
    """
    This class defines the user model

    :param id: (int) id of occurrence, primary key, generated automatically 
    :param id_user: (int) id of user
    :param description: (string) description of the occurrence
    :param date_created: (datetime) date of creation, default=datetime.now()
    :param date_updated: (datetime) updated date, default=datetime.now()
    :param state: (int) state of the occurrence, default=0
    :param category: (string) category of the occurrence
    :param latitude: (float) latitute
    :param longitude: (float) longitude
    :param distance: (float) distance of the occurrence to the ubiwhere hq
    """

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(22), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)

    def __init__(self, id_user, description, category, latitude, longitude, distance):
        self.id_user = id_user
        self.description = description
        self.date_created = datetime.now()
        self.date_updated = datetime.now()
        self.state = 0
        self.category = category
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance

    def __repr__(self):
        return "<Occurrence %r>" % self.description

