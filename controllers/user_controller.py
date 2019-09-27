from main import app, db, auth
from git import Repo
from flask import request, jsonify
from models.user import User


repo = Repo()


@app.route("/check_password", methods=["GET"])
@auth.login_required
def check_password():
    return jsonify({"status": "request went through"})
@app.route("/user", methods=['POST'])
def create_user():
    content = request.json #only works if content type is application/json
    name = content["username"]
    pwd = content["password"]
    user = User(username=name)
    user.set_password(pwd)
    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "created", "user": {"name": user.username}})
