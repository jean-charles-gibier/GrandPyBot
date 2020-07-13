"""
vue de l'application
"""
from flask import Flask, render_template, request
from .utils import Question

APP = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
APP.config.from_object('config')


@APP.route('/')
@APP.route('/index/')
def index():
    """ main route """
    return make_index()

@APP.route('/ask', methods=['POST'])
def ask():
    """ pass asking question to be answered """
    return make_answer()

def make_answer():
    """ build an answer """
    try:
        if request.method == 'POST':
            input_question = request.form.to_dict()
            whole_question = input_question.popitem()[0]
            short = Question(whole_question).get_shortened_question()
            print("Had to answer 2 : {} ".format(short))
    except:
        print("Probleme")
        return 'None'
    return render_template('index.html')


def make_index():
    """ joue la page d'index """
    return render_template('index.html')


