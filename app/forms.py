from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = EmailField("Email address", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(5, 100, message="Liczba znakow musi byc miedzy 5 a 100!")])

    submit = SubmitField("Sign in")