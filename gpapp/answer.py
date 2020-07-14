"""
Utilitaires *
 - traitement output
"""
from .question import Question
from .google_api import GoogleApi
from .wiki_media_api import WikiMediaApi

class Answer:
    """
    Builds an answer from question
    """

    def __init__(self, question):
        """ init """
        self.short = question.get_shortened_question()
        # get info from

    def fetch_infos_from_google_map(self, infos):
        """
        getter info from gg (gps coordinates 1rst)
        """


        return

    def fetch_infos_from_wiki_media(self, infos):
        """
        suppress stop words (+ some) and ponctuation
        """
        return

    def get_final_infos(self):
        """
        prepare display values
        """
        return self.short
