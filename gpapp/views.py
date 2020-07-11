"""
vue de l'application
"""
from flask import Flask, render_template \
    # , url_for, request

APP = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
APP.config.from_object('config')


@APP.route('/')
@APP.route('/index/')
def index():
    """ main route """
    return make_index()


def make_index():
    """ joue la page d'index """
    return render_template('index.html')
