from app import app
from flask import render_template


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error/500.html'), 500