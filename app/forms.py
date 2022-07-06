
from unicodedata import digit
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from re import search

def password_check(form, field):

    # Password must be between 10 and 100 characters
    if len(field.data) < 10 or len(field.data) > 100:
        raise ValidationError("Must be between 10 and 100 characters!")

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
    email = EmailField("Email address", validators=[DataRequired(), Length(max=100), Email()])
    password = PasswordField("Password", validators=[DataRequired(), password_check])
    

    submit = SubmitField("Sign in")