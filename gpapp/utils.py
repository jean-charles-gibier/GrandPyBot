"""
Utilitaires
"""

class Question:
    """
    handle the content of question to build an answer
    """

    def __init__(self):
        self.whole_question = ""

    @staticmethod
    def answer():
        """
        analyze & parse to return an answer
        """
        return "fake answer"

    def another_method(self):
        """ just to avoid lint error """
        return "dummy" +self.whole_question
