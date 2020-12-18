from flask import Flask,jsonify,g
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import *

import models
from resources.shirts import shirt
from resources.jackets import jacket
from resources.pants import pant
from resources.shoes import shoe
from resources.users import user

DEBUG = True
PORT = process.env.port

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.secret_key = process.env.secret
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.Users.get(models.Users.id == userid)
    except models.DoesNotExist:
        return None

#LLogic for our dtatbase connection
@app.before_request
def before_request():
    """Connect to the database befoe the request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close db after request"""
    g.db.close()
    return response

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)