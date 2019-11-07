"""
.. module:: auth
   :synopsis: All the endpoints regarding the authentication, are defined here
.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>
"""


from flask import request, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

from ubiwhere_challenge import db, login_manager
from ubiwhere_challenge.models import User


auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route("/register", methods=["POST", "GET"])
def register():
    """
    Register new user, if the request is successful.

    :returns: The creater user
    :rtype: json
    """

    if request.method == "POST":

        # Get the Json data form body request
        user_json = request.get_json(force=True)

        # Assign the values to variables
        username = user_json["username"]
        name = user_json["name"]
        email = user_json["email"]
        password = generate_password_hash(
            user_json["password"], method="sha256")

        # Query the user to verify if exists
        user = User.query.filter_by(email=user_json["email"]).first()

        if user:
            # The user exists, return error
            return {"error": "The user exist in the database"}
        else:
            # Create new user
            user_db = User(username=username, name=name,
                           email=email, password=password)

        # Add the user to the DB
        db.session.add(user_db)
        db.session.commit()
    return {"code": 200, "description": "The user was successful created"}


@auth.route("/login", methods=["POST", "GET"])
def login():
    """
    Login user, if the request is successful.

    :returns: Request result, in the json format
    :rtype: json
    """

    if request.method == "POST":

        # Get the Json data form body request
        user_json = request.get_json(force=True)

        print(user_json)

        # Assign the values to variables
        email = user_json["email"]
        password = user_json["password"]

        # Query the user to verify if exists
        user = User.query.filter_by(email=email).first()

        # If the user does not exist or the password is wrong
        if not user or not check_password_hash(user.password, password):
            return {"error": "bad credentials"}
        else:
            login_user(user, duration=timedelta(hours=1))

    return {"code": 200, "description": "The user was successful logged in"}


@auth.route('/logout')
@login_required
def logout():
    """
    Logout user, if the request is successful.

    :returns: Request result, in the json format
    :rtype: json
    """

    logout_user()
    return {"sucess": "User logged out"}
