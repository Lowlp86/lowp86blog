from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#init t flask app
app = Flask(__name__)
app.config.from_object('config')

#init SQL
db = SQLAlchemy(app)

#init flask-Login
lm = LoginManager()
lm.setup_app(app)

from app import views, models
