from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost:3306'
db = SQLAlchemy(app)


from controllers.status_controller import *
from controllers.events_controller import *
from controllers.user_controller import *

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
