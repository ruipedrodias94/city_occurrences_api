from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost/teste'

db = SQLAlchemy(app)

from ubiwhere_challenge import routes