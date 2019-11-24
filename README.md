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
# PRE-REQUISITES
You must have the Flutter SDK installed (see https://flutter.dev/docs/get-started/install) along with Android Studio. Setup a server with a connection to a MySQL dataset.
# DEPENDENCIES
Download and install Flask (see http://flask.palletsprojects.com/en/1.1.x/installation/#installation)
The list of dependencies for Flask are in the pubspec.yaml file.
 
For the serverside use the env.yaml file. Install conda and use the following commands on a server with an open connection to the internet or with a connection to a router connected to the internet.
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
 ./Miniconda3-latest-Linux-x86_64.sh -b
 conda env create -f env.yaml
# DOWNLOAD
	https://github.com/techlanta/LetsPlayAtl/archive/master.zip
	https://github.com/techlanta/LetsPlayATLServer/archive/v1.0.zip
# BUILD
	No build necessary.
# INSTALLATION
	
# RUNNING APPLICATION
  Use Android or iPhone with Android Studio or with XCode
	Any text editor (see https://flutter.dev/docs/get-started/editor)

