from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, ValidationError, EqualTo
from re import search

from app.models import User


def password_check(form, field):

    # Password must be between 10 and 100 characters
    if len(field.data) < 10 or len(field.data) > 128:
        raise ValidationError("Must be between 10 and 128 characters!")

    # searching for uppercase
    uppercase_error = search(r'[A-Z]', field.data) is None
    if uppercase_error:
        raise ValidationError("Must have at least 1 uppercase character!")
        
    # searching for lowercase
    lowercase_errror = search(r'[a-z]', field.data) is None
    if lowercase_errror:
        raise ValidationError("Must have at least 1 lowercase character!")

    # searching for digit
    digit_error = search(r'\d', field.data) is None
    if digit_error:
        raise ValidationError("Must have at least 1 digit!")

    #searching for symbol
    symbol_error = search(r'\W', field.data) is None
    if symbol_error:
        raise ValidationError("Must have at least 1 special symbol!")



class LoginForm(FlaskForm):

    # Checks if email and passwords are correct
    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user or not user.check_password(self.password.data):
            raise ValidationError("Invalid email or username!")

    email = EmailField("Email address", validators=[InputRequired(), Length(max=128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=128)])

    submit = SubmitField("Sign in")
        

class RegisterForm(FlaskForm):

    # Checks if email is in database
    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Email has been already taken!")

    # Checks if username is in database
    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username has been already taken!")

    email = EmailField("Email address", validators=[InputRequired(), Length(max=128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=128), password_check])
    username = StringField("Username", validators=[InputRequired(), Length(min=5, max=32)])
    confirm_password = PasswordField("Confirm password", validators=[InputRequired(),EqualTo('password', message='Passwords do not match!')])

    

    submit = SubmitField("Register now")