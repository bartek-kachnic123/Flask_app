from flask_login import UserMixin
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login.user_loader
def user_loader(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True, nullable = False)
    email = db.Column(db.String(128), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)

    # Hash password
    def hash_password(self, password):
        self.password = generate_password_hash(password)
    
    # Checks if hashed password is equal to input password
    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)

    
        

class Patient(db.Model):
    __tablename__ = "Patients"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    firstname = db.Column(db.String(64), nullable = False)
    lastname = db.Column(db.String(64), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    status = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
