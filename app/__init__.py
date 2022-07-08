from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

from app import views, admin_views




