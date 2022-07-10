from flask_login import UserMixin
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

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
    def hash_password(self):
        self.password = generate_password_hash(self.password)
    
    # Checks if hashed password is equal to input password
    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)

    
        

    