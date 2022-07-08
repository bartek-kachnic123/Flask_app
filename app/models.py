from app import db


class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, user, email, passd) -> None:
        self.username = user
        self.email = email
        self.password = passd