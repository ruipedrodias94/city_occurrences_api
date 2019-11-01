from flask_restful import Resource, Api
from ubiwhere_challenge import app

api = Api(app)


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


class HelloWorld(Resource):
    def get(self):
        return {"hello": "World"}

api.add_resource(HelloWorld, "/");