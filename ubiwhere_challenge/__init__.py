"""
This module creates the application and returns it

.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import os

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

def create_app():

    # Create the flask app
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)

    # Configuration for the database
    app.config["SECRET_KEY"] = "334c366877247985dd22616feeef4141"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost/local_database"

    # Import the blueprints
    from ubiwhere_challenge.auth.routes import auth
    from ubiwhere_challenge.occurrences.routes import occurrences
    from ubiwhere_challenge.errors.errors_handler import error_handler
    app.register_blueprint(auth)
    app.register_blueprint(occurrences)
    app.register_blueprint(error_handler)

    return app