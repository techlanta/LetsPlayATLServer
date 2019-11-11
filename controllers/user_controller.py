from main import app, db, auth
from git import Repo
from flask import request, jsonify
from models.user import User
import models.user



repo = Repo()


@app.route("/check_password", methods=["POST"])
def check_password():
    content = request.json #only works if content type is application/json
    pwd = content["password"]
    username = content["username"]
    status = models.user.verify_password(username, pwd)
    if status is not None and status == True:
        user = User.query.filter_by(username=username).first()
        fullname= user.fullname
        is_admin = user.is_admin
    else:
        status = False
        fullname = "incorrect credentials"
        is_admin = False
    return jsonify({"status": status, "fullname": fullname, "is_admin": is_admin})

@app.route("/user", methods=['POST'])
def create_user():
    content = request.json #only works if content type is application/json
    name = content["username"]
    userAlreadyExist = User.query.filter_by(username=name).count() == 1
    if userAlreadyExist:
        return jsonify({"status": "User already exist", "user": {"name": "User already exist"}})

    if "fullname" in content:
        fullname = content["fullname"]
    else:
        fullname = "citizen"
    pwd = content["password"]
    if "is_admin" in content:
        is_admin = content["is_admin"]
    else:
        is_admin = False
    user = User(username=name, fullname=fullname, is_admin=is_admin)
    user.set_password(pwd)
    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "created", "user": {"name": fullname, "username": user.username}})
