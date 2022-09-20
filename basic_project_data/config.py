import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'basic_flask_project_key'
    APP_NAME = os.environ.get('APP_NAME') or 'Basic Flask Project'
