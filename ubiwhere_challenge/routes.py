from flask_restful import Resource, Api, reqparse
from ubiwhere_challenge import app, db
from ubiwhere_challenge.models import User
import json

api = Api(app)


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

parser = reqparse.RequestParser()
parser.add_argument('user')


class HelloWorld(Resource):
    def get(self):
        return {"hello": "World"}

class NewUser(Resource):
    def get(self):
        return db

    def post(self):
        args = parser.parse_args()
        newUser = json.loads(args["user"])
        me = User(username="username1", email="email1")
        #user = User(newUser["username"], newUser["email"], newUser["name"])
        db.session.add(me)
        db.session.commit()
        return newUser


api.add_resource(HelloWorld, "/");
api.add_resource(NewUser, "/newUser")