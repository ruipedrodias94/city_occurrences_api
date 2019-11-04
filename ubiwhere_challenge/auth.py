from flask import request
from ubiwhere_challenge import app, db, login_manager
from ubiwhere_challenge.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method=="POST":

        # Get the Json data form body request
        user_json = request.get_json(force=True)

        # Assign the values to variables
        username = user_json["username"]
        name = user_json["name"]
        email = user_json["email"]
        password = generate_password_hash(user_json["password"], method="sha256")

        # Query the user to verify if exists
        user = User.query.filter_by(email=user_json["email"]).first()
        
        if user:
            # The user exists, return error 
            pass
        else:
            # Create new user
            user_db = User(username=username, name=name, email=email, password=password)
            print(user_db)
        
        # Add the user to the DB
        db.session.add(user_db)
        db.session.commit()
    return user_json



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":

        # Get the Json data form body request
        user_json = request.get_json(force=True)

        # Assign the values to variables
        email = user_json["email"]
        password = user_json["password"]

        # Query the user to verify if exists
        user = User.query.filter_by(email=email).first()
        
        if not user and not check_password_hash(user.password, password):
            return {"error": "bad credentials"}
        else:
            login_user(user)
        
        print(current_user.id)

    return {"sucess": "User logged in"}


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return {"sucess": "User logged out"}