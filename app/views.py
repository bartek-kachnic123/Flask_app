from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

# Main site
@app.route('/')
@app.route('/index')
def index():
    return render_template('/public/dashboard.html')

# User profile
@app.route('/profile/<username>')
@login_required
def profile(username):

    # If user is not found, return 404 error
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('private/profile.html', user=user)

# Sign up operation
@app.route('/register', methods=['GET', 'POST'])
def register():

    # if user is already logged
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():

        # Creating user
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # Hashing password
        user.hash_password()
        # Adding user to database
        db.session.add(user)
        db.session.commit()
        
        flash('You successfully made account! Now you can log in!', category='success')
        return redirect(url_for('login'))
    
    return render_template('/public/register.html', form = form)


# Sign in operation
@app.route('/login', methods=['GET', 'POST'])
def login():

    # if already logged
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        
        # Login user
        user = User.query.filter_by(email=form.email.data).first()
        # Login user with remember option
        login_user(user, remember=form.remember_me.data)
        flash('You have successfully logged in!', category='success')

        # get query string 'next' attr
        next_page = request.args.get('next')

        # if next page doesnt exist or if url includes full path with domain name
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('index'))
        return redirect(next_page)

    return render_template('/public/login.html', form = form)


# Logout operation
@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('login'))
