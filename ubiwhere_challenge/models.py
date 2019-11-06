"""
.. module:: models
   :synopsis: All the models used to represent the objects
.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>
"""

from flask_sqlalchemy import SQLAlchemy
from ubiwhere_challenge import db, ma
from flask_login import UserMixin
from datetime import datetime
import os


"""
In this package will be defined the database models
"""

class User(db.Model, UserMixin):

    """
    User model

    :param id: Author id
    :type id: int
    :param username: Username
    :type username: str
    :param email: Email
    :type email: str
    :param password: Password
    :type password: str
    :param occurrences: Occurrences
    :type occurrences: Occurrence
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
    Occurrence model

    :param id: Id of occurrence
    :type id: int
    :param id_user: Id of user
    :type id_user: int
    :param description: Description of the occurrence
    :type description: str
    :param date_created: Date of creation, default=datetime.now()
    :type date_created: datetime
    :param date_updated: Updated date, default=datetime.now()
    :type date_updated: datetime
    :param state: State of the occurrence, default=0
    :type state: int
    :param category: Category of the occurrence
    :type category: str
    :param latitude: Latitute
    :type latitude: float
    :param longitude: Longitude
    :type longitude: float
    :param distance: Distance of the occurrence
    :type distance: float
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


class UserSchema(ma.ModelSchema):
    """
    User Schema - Marsmallow
    """

    class Meta:
        model = User

class OccurrenceSchema(ma.ModelSchema):
    """
    Occurrence Schema - Marsmallow
    """
    
    class Meta:
        model = Occurrence