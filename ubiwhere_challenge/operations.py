from flask import request, jsonify
from ubiwhere_challenge import app, db, login_manager
from ubiwhere_challenge.models import User, Occurrence
from datetime import datetime
from flask_login import login_required, current_user, user_logged_in
from geopy import distance

# Ubiwhere Headquarters - Used to calculate the distance between the occurrences
ubiwhere_hq = {
    "latitude": 40.646860,
    "longitude": -8.643030
}

def calc_distance_in_km(hq, point):
    point_one = (hq["latitude"], hq["longitude"])
    point_two = (point["latitude"], point["longitude"])
    print(distance.distance(point_one, point_two).km)
    return distance.distance(point_one, point_two).km


@app.route("/occurrence/create", methods=["GET", "POST"])
@login_required
def create_occurrence():
    if request.method == "POST":

        # Get the Json data form body request
        occurrence_json = request.get_json(force=True)

        # Assign the values to variables
        description_request = occurrence_json["description"]
        category_request = occurrence_json["category"]
        location_request = occurrence_json["location"]

        # Create the occurrence instance
        occurrence_db = Occurrence(id_user=current_user.id, description=description_request, category=category_request,
                                   latitude=location_request["latitude"], longitude=location_request["longitude"],
                                   distance=calc_distance_in_km(ubiwhere_hq, location_request))

        # Add the occurrence to the db
        db.session.add(occurrence_db)
        db.session.commit()

        return occurrence_json


@app.route("/occurrences/filter_by_author/<int:id_user>", methods=["GET"])
@login_required
def get_occurrences_by_author(id_user):

    occurrences = {}

    occurrence_db = Occurrence.query.filter_by(id_user=id_user).all()
    
    for occurrence in occurrence_db:

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
    

@app.route("/occurrence/<int:occurrence_id>/update", methods=["POST"])
@login_required
def update_occurrence_by_id(occurrence_id):
    
    occurrence_db = Occurrence.query.filter_by(id=occurrence_id).first()
    
    if current_user.id == 1:
        
        occurrence_db.state = request.form["state"]
        occurrence_db.date_updated = datetime.now()

    else: 
        pass

    db.session.commit()

    return {"status": "updated"}


@app.route("/occurrences", methods=["GET"])
def get_occurrences():
    """
    This function will return all the occurrences inserted in the system
    :param: None
    :return: dict {}, All the occurrences
    """
    occurrences = {}

    occurrence_db = Occurrence.query.order_by(Occurrence.date_created).all()

    for occurrence in occurrence_db:
        occurrence_model = {}

        occurrence_model["id"] = occurrence.id
        occurrence_model["author_id"] = occurrence.id_user
        occurrence_model["description"] = occurrence.description
        occurrence_model["date_created"] = occurrence.date_created
        occurrence_model["date_updated"] = occurrence.date_updated
        occurrence_model["state"] = occurrence.state
        occurrence_model["latitude"] = occurrence.latitude
        occurrence_model["longitude"] = occurrence.longitude
        occurrence_model["distance"] = occurrence.distance

        occurrences[str(occurrence.id)] = occurrence_model

    return jsonify(occurrences)
