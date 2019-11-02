from flask import request
from ubiwhere_challenge import app, db
from ubiwhere_challenge.models import User
import json

user = {
    "username": "username",
    "email": "email",
    "name": "name"
}

occurrence = {
    "id": "1",
    "description": "This is an example",
    "geolocation": (10, 1),
    "author": "Rui Dias",
    "creation_date": 2019,
    "update_date": 2019,
    "state": 0,
    "category": 0
}

occurrences = [
    {
        "id": "1",
        "description": "This is an example",
        "geolocation": (10, 1),
        "author": "Rui Dias",
        "creation_date": 2019,
        "update_date": 2019,
        "state": 0,
        "category": 0
    },
    {
        "id": "2",
        "description": "This is an example",
        "geolocation": (12, 12),
        "author": "Antone",
        "creation_date": 2019,
        "update_date": 2019,
        "state": 0,
        "category": 0
    }
]

@app.route("/", methods=["GET"])
def helloWorld():
    return {"hello"}

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method=="POST":
        user_json = request.get_json(force=True)
        user_db = User(username=user_json["username"], email=user_json["email"])
        db.session.add(user_db)
        db.session.commit()
    return user_json
