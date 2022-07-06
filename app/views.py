from app import app
from flask import render_template, request, redirect, flash
from app.forms import LoginForm
@app.route('/')
def index():
    return render_template('/public/dashboard.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        
        for key, name in request.form.items():
            print(key, name)
        return redirect('/sign_up') # zmienic przekierowanie na sign_in
    
    return render_template('/public/sign_up.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f'You have sucessfully logged in!', category="success")
        return redirect('/')
    # Any login error
    elif form.is_submitted() and not form.validate():
        for key, info in form.errors.items():
            flash(f'{key.capitalize()} - {" - ".join(info)}', category='warning')
    return render_template('/public/login.html', form = form)
