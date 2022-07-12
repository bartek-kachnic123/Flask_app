from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment



app = Flask(__name__)

# APP
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

# Database
db = SQLAlchemy(app)

# Login
login = LoginManager(app)
login.login_view = 'login'

# Moment (Time zone)
moment = Moment(app)

from app import views, admin_views




