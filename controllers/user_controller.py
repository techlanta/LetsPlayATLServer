from main import app, db
from git import Repo

repo = Repo()


@app.route("/login", methods=["POST"])
def login():
    return "NOT IMPLEMENTED"

@app.route("/user", methods=['POST'])
def events():
    content = request.json #only works if content type is application/json
    name = content["name"]
    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "created", "user": {"name": name, "id": user.id}})
