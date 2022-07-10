from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms import LoginForm, RegisterForm
from app.models import User

# Main site
@app.route('/')
@app.route('/index')
def index():
    return render_template('/public/dashboard.html')


# Sign up operation
@app.route('/register', methods=['GET', 'POST'])
def register():
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
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('You have successfully logged in!', category="success")
        return redirect(url_for('index'))
    

    return render_template('/public/login.html', form = form)
