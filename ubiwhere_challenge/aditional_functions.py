from flask import jsonify
from geopy import distance

def calc_distance_in_km(hq, point):
    point_one = (hq["latitude"], hq["longitude"])
    point_two = (point["latitude"], point["longitude"])
    print(distance.distance(point_one, point_two).km)
    return distance.distance(point_one, point_two).km

def parse_query(query):

    occurrences = {}

    for occurrence in query:

        occurrence_model = {}

        occurrence_model["id"] = occurrence.id
        occurrence_model["author_id"] = occurrence.id_user
        occurrence_model["description"] = occurrence.description
        occurrence_model["date_created"] = occurrence.date_created
        occurrence_model["date_updated"] = occurrence.date_updated
        occurrence_model["state"] = occurrence.state
        occurrence_model["category"] = occurrence.category
        occurrence_model["latitude"] = occurrence.latitude
        occurrence_model["longitude"] = occurrence.longitude
        occurrence_model["distance"] = occurrence.distance

        occurrences[str(occurrence.id)] = occurrence_model

    return jsonify(occurrences)