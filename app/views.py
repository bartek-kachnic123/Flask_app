from app import app
from flask import render_template, request, redirect
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