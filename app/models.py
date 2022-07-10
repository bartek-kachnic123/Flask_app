from sqlalchemy import null
from app import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

    