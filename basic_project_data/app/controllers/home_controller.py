from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/home/index')
def index():
    #
    return render_template(
        "home/index.html",
        )

@app.route('/about')
def about():
    return render_template('home/about.html')

@app.route('/contact')
@app.route('/home/contact')
def contact():
    #...
    return render_template(
        'error/404.html'
        ), 404