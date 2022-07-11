from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, ValidationError, EqualTo
from re import search

from app.models import User



class LoginForm(FlaskForm):

    email = EmailField("Email address", validators=[InputRequired(), Length(max=128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=128)])
    submit = SubmitField("Sign in")

    # Checks if email and passwords are correct
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user or not user.check_password(self.password.data):
            raise ValidationError("Invalid email or username!")
        

class RegisterForm(FlaskForm):

    email = EmailField("Email address", validators=[InputRequired(), Length(max=128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=128)])
    username = StringField("Username", validators=[InputRequired(), Length(min=5, max=32)])
    confirm_password = PasswordField("Confirm password", validators=[InputRequired(),EqualTo('password', message='Passwords do not match!')])
    submit = SubmitField("Register now")

    # Checks if email is in database
    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Email has been already taken!")

    # Checks if username is in database
    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username has been already taken!")

    # Checks password requirements
    def validate_password(self, password):
        # Password needs :
            # a) One or more upper letters
            # b) One or more lower letters
            # c) One or more digits
            # d) One or more special character


        # searching for uppercase
        uppercase_error = search(r'[A-Z]', password.data) is None
        if uppercase_error:
            raise ValidationError("Must have at least 1 uppercase character!")
            
        # searching for lowercase
        lowercase_errror = search(r'[a-z]', password.data) is None
        if lowercase_errror:
            raise ValidationError("Must have at least 1 lowercase character!")

        # searching for digit
        digit_error = search(r'\d', password.data) is None
        if digit_error:
            raise ValidationError("Must have at least 1 digit!")

        #searching for symbol( not word character)
        symbol_error = search(r'\W', password.data) is None
        if symbol_error:
            raise ValidationError("Must have at least 1 special symbol!")