from flask import Flask, request, jsonify
from git import Repo
import controllers.events_controller as events_c
app = Flask(__name__)

repo = Repo()

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    global repo
    sha = repo.head.object.hexsha
    return repo.git.rev_parse(sha, short=8)

@app.route("/events", methods=['POST'])
def events():
    content = request.json #only works if content type is application/json
    return jsonify(events_c.create(content["name"]))


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
