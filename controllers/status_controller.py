from main import app, db
from git import Repo
from models.sdg import ALL_SDG

repo = Repo()

@app.route("/health")
def health():
    return "OK"

@app.route("/drop_all")
def drop_all():
    db.drop_all()
    return {"status": "completed"}

# @app.route("/reset_all")
# def reset_all():
#     db.create_all()
#
#     db.session.commit()
#
#     return {"status": "completed"}

@app.route("/reset")
def reset():
    db.drop_all()
    db.create_all()
    for sdg in ALL_SDG:
        db.session.add(sdg)
    db.session.commit()
    return {"status": "completed"}

@app.route("/version")
def version():
    global repo
    sha = repo.head.object.hexsha
    return repo.git.rev_parse(sha, short=8)
