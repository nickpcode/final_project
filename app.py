from flask import Flask,jsonify,g
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
# from flask_login import LoginManager

import os
import models
from resources.shirts import shirt
from resources.jackets import jacket
from resources.pants import pant
from resources.shoes import shoe
# from resources.users import user

DEBUG = True
PORT = os.getenv('PORT')

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.secret_key = os.getenv('SECRET')
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(userid):
#     try:
#         return models.Users.get(models.Users.id == userid)
#     except models.DoesNotExist:
#         return None

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

CORS(shirt, origins='*', supports_credentials=True)
CORS(jacket, origins='*', supports_credentials=True)
CORS(pant, origins='*', supports_credentials=True)
CORS(shoe, origins='*', supports_credentials=True)


app.register_blueprint(shirt, url_prefix='/api/v1/shirts')
app.register_blueprint(jacket, url_prefix='/api/v1/jackets')
app.register_blueprint(pant, url_prefix='/api/vi/pants')
app.register_blueprint(shoe, url_prefix='/api/vi/shoes')
# app.register_blueprint(user, url_prefix='/user')


# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)