"""
.. module:: occurrences
   :synopsis: Here are defined all the extra functions related to the occurrence object
.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>
"""


from flask import jsonify
import json
from geopy import distance
import collections
from datetime import datetime
import os

from ubiwhere_challenge.models import OccurrenceSchema


def calc_distance_in_km(hq, point):
    """
    Calculates the distance between a given point and the ubiwhere hq
    
    :param hq: Headquarters object
    :type hq: dict
    :param point: New point object
    :type point: dict
    :returns: Distance between the two points
    :rtype: float
    """

    point_one = (hq["latitude"], hq["longitude"])
    point_two = (point["latitude"], point["longitude"])
    print(distance.distance(point_one, point_two).km)
    return distance.distance(point_one, point_two).km


def return_json(query):
    """
    Calculates the distance between a given point and the ubiwhere hq
    
    :param query: The database query
    :type hq: Class Sqlalchemy
    :returns: Object query serialized to json
    :rtype: list
    """

    occurrence_model = OccurrenceSchema(many=True)
    output = occurrence_model.dump(query)
    print (type(output))
    return output