"""
Appel de l'appli GdPy
+ methodes CLI
ask_from_cli, passage question from command line
"""
from .views import APP
from .utils import Question

@APP.cli.command()
def ask_from_cli():
    """ appel ask_question via CLI """
    Question.answer()
