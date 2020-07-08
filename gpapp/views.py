"""
vue de l'application
"""
from flask import Flask

# , render_template, url_for, request

APP = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
APP.config.from_object('config')


# To get one variable, tape app.config['MY_VARIABLE']

# from .utils import find_content

@APP.route('/')
@APP.route('/index/')
def index():
    """ main route """
    return 'Hello, World!'
