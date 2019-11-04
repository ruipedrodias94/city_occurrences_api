from flask import request, jsonify
from ubiwhere_challenge import app, db, login_manager
from ubiwhere_challenge.models import User, Occurrence
from ubiwhere_challenge.aditional_functions import calc_distance_in_km, parse_query
from datetime import datetime
from flask_login import login_required, current_user, user_logged_in


# Ubiwhere Headquarters - Used to calculate the distance between the occurrences
ubiwhere_hq = {
    "latitude": 40.646860,
    "longitude": -8.643030
}


@app.route("/occurrence/", methods=["GET", "POST"])
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


@app.route("/occurrences/author/<int:id_user>", methods=["GET"])
@login_required
def get_occurrences_by_author(id_user):

    occurrence_db = Occurrence.query.filter_by(id_user=id_user).all()
    
    occurences = parse_query(occurrence_db)
    
    return occurences
    

@app.route("/occurrences/category/<string:category>", methods=["GET"])
@login_required
def get_occurrences_by_category():

    category = request.args["category"]

    occurrence_db = Occurrence.query.filter_by(category=(category)).all()
    
    occurences = parse_query(occurrence_db)
    
    return occurences


@app.route("/occurrences/distance/<int:distance>", methods=["GET"])
@login_required
def get_occurrences_by_location():

    distance = request.args["distance"]

    occurrence_db = Occurrence.query.filter(Occurrence.distance<=distance)
    
    occurences = parse_query(occurrence_db)
    
    return occurences


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

    occurrence_db = Occurrence.query.order_by(Occurrence.date_created).all()

    occurrences = parse_query (occurrence_db)

    return occurrences


