from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from google.appengine.ext import db

app = Flask(__name__)
app.config.from_object('app_config')

# HOME PAGE
from app.mod_home.controller import mod_home as home
app.register_blueprint(home)
