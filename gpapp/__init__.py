"""
Appel de l'appli GdPy
+ methodes CLI
ask_from_cli, passage question from command line
"""
import click

from .views import APP
from .utils import Question

@APP.cli.command()
@click.argument("question")
def ask_from_cli(question):
    """ appel ask_question via CLI """
    print(Question(question).get_shortened_question())
