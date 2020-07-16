"""
vue de l'application
"""
from flask import Flask, render_template, request, jsonify
from .question import Question
from .answer import Answer

APP = Flask(__name__)
#  'config.py' file a completer.
APP.config.from_object('config')


@APP.route('/')
@APP.route('/index/')
def index():
    """ main route """
    return make_index()


@APP.route('/ask', methods=['GET', 'POST'])
def ask():
    """ pass asking question to be answered
        request : json value to parse
     """
    return make_answer()


def make_answer():
    """ build an answer from a request content """
    try:
        if request.method == 'POST':
            input_question = (request.form.to_dict())['papyFormText']
            answer = Answer(Question(input_question))
            final_infos = answer.get_final_infos()

    except Exception as e:
        print("Probleme :" + str(e))
        return jsonify({'output': 'Oups ! GrandPy a eu une petite absence.'})

    return jsonify({'output': final_infos})


def make_index():
    """ joue la page d'index """
    return render_template('index.html')
