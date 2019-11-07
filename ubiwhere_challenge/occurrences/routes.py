"""
.. module:: occurrences
   :synopsis: All the endpoints regarding the occurrences, are defined here
.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>
"""

from flask import request, jsonify, Blueprint, abort
from datetime import datetime
from flask_login import login_required, current_user, user_logged_in
import os

from ubiwhere_challenge import db, login_manager
from ubiwhere_challenge.models import User, Occurrence, UserSchema, OccurrenceSchema
from ubiwhere_challenge.errors.errors_handler import forbidden, resource_not_found, error_500

from ubiwhere_challenge.occurrences.utils import calc_distance_in_km, return_json

occurrences = Blueprint("occurrences", __name__)


@occurrences.route("/occurrence/", methods=["GET", "POST"])
@login_required
def create_occurrence():
    """
    Create new occurrences, if the request is successful

    :returns: Result code of the request
    :rtype: list
    """

    ubiwhere_hq = {
        "latitude": 40.646860,
        "longitude": -8.643030
    }

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

        if occurrence_db:
            # Add the occurrence to the db
            db.session.add(occurrence_db)
            db.session.commit()

        else:
            # The object was not created an could not be added to the database
            return {"error": "The object occurrence could not be created, and it wasn't added to the database"}

        return {"code": 200, "description": "The occurrence was successful created"}


@occurrences.route("/occurrences/author/<int:id_user>", methods=["GET"])
@login_required
def get_occurrences_by_author(id_user):
    """
    Query occurrences by author, if the request is successful

    :param id_user: Author id
    :type id_user: int
    :returns: Occurrences
    :rtype: list
    """

    # Query the database
    occurrence_db = Occurrence.query.filter_by(id_user=id_user).all()

    output = return_json(occurrence_db)

    if not output:
        return {"code": 200, "description": "Could not find any occurrences with that author"}

    return jsonify(output)


@occurrences.route("/occurrences/category/<string:category>", methods=["GET"])
@login_required
def get_occurrences_by_category(category):
    """
    Query occurrences by category, if the request is successful

    :param category: Occurrence Category
    :type category: str
    :returns: Occurrences
    :rtype: list
    """

    # Query the database
    occurrence_db = Occurrence.query.filter_by(category=category).all()

    output = return_json(occurrence_db)

    if not output:
        return {"code": 200, "description": "Could not find any occurrences with that category"}

    return jsonify(output)


@occurrences.route("/occurrences/distance/<int:distance>", methods=["GET"])
@login_required
def get_occurrences_by_location(distance):
    """
    Query occurrences by distance, if the request is successful

    The occurrences are returned if the distance is less or equal than the distance in arguments

    :param distance: Distance to Headquarters
    :type distance: int
    :returns: Occurrences
    :rtype: list
    """

    # Query the database
    occurrence_db = Occurrence.query.filter(Occurrence.distance <= distance)

    output = return_json(occurrence_db)

    if not output:
        return {"code": 200, "description": "Could not find any occurrences to that distance"}

    return jsonify(output)


@occurrences.route("/occurrence/<int:occurrence_id>/update", methods=["POST"])
@login_required
def update_occurrence_by_id(occurrence_id):
    """
    Update the state of the occurrence with the id passed by argument.

    :param occurrence_id: Id of the occurrence
    :type occurrence_id: int
    :returns: Code of request
    :rtype: list
    """

    # Query the database
    occurrence_db = Occurrence.query.filter_by(id=occurrence_id).first()

    # If user is Admin (Hardcoded)
    if current_user.id == 1:

        # If exists
        if occurrence_db:
            occurrence_db.state = request.form["state"]
            occurrence_db.date_updated = datetime.now()
            db.session.commit()
        else:
            return {"code": 200, "description": "Could not find any occurrence with that id"}
    else:
        return forbidden(403, "The user has not permission to complete the request")

    return {"code": 200, "description": "The occurrence was successful updated"}


@occurrences.route("/occurrences", methods=["GET"])
def get_occurrences():
    """
    Return all the occurrences in the system

    :returns: Occurrences
    :rtype: list
    """

    # Query the database
    occurrence_db = Occurrence.query.order_by(Occurrence.date_created).all()

    output = return_json(occurrence_db)

    if not output:
        return {"code": 200, "description": "Could not find any occurrences in the database"}

    return jsonify(output)
