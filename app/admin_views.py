from app import app

@app.route('/admin')
def admin_site():
    return "<h1>Admin</h1>"