from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:root@localhost/local_database'

db = SQLAlchemy(app)

from ubiwhere_challenge import routes