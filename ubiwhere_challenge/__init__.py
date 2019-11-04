from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "334c366877247985dd22616feeef4141"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost/local_database"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from ubiwhere_challenge import auth
from ubiwhere_challenge import operations
from ubiwhere_challenge import models