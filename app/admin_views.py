from flask import render_template
from app import app
from flask import render_template

@app.route('/admin')
def admin_site():
    return render_template('/admin/admin_dashboard.html')