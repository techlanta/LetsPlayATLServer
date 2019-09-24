from main import app, db
from git import Repo

repo = Repo()

@app.route("/health")
def health():
    return "OK"

@app.route("/reset")
def reset():
    db.drop_all()
    db.create_all()
    return {"status": "completed"}

@app.route("/version")
def version():
    global repo
    sha = repo.head.object.hexsha
    return repo.git.rev_parse(sha, short=8)
