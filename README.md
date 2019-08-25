# LetsPlayATLServer
AWS Server App run in EC2
This is a server app which exposes CRUD methods for community events for the LetsPlayATL Flutter App.

# How to run
https://stackoverflow.com/questions/16344756/auto-reloading-python-flask-app-upon-code-changes

Secrets are stored in config.json, which is NEVER saved into git.
```
{
  "firebase_api_key": "api_key"
}
```

Run this command:

``` bash
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run
```
