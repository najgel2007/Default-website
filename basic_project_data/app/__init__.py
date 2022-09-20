from flask import Flask, send_from_directory
from flask_bootstrap import Bootstrap
from config import Config
import os


app =Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

from app.controllers import home_controller
from app import errors
from app import cookies