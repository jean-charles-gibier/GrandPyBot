"""
Utilitaires *
 - traitement input
"""

import re
from stop_words import get_stop_words


class Question:
    """
    handle the content of question to build an answer
    """

    def __init__(self, question):
        """ init """
        common_words = {'bonjour', 'salut', 'hello', 'ciao', 'yo', 'hi',
                        'dis', 'moi', 'he', 'au', 'fait', 'ca', 'va', 'se',
                        'bon', 'quel', 'quelle', 'où', 'est-ce', 'que', 'ce',
                        'connais', 'connaissez', 'sais', 'savez', 'saurais',
                        'grandpy', 'grand-père', 'papy', 'cher', 'mec', 'ou',
                        'adresse', 'lieu', 'localisation', 'endroit', 'trouve',
                        'aller', 'vers', 'comment', 'stp', 'wesh', 's\'il',
                        'te', 'plait', 'steup', 'gd', 'py', 'gdpy'
                        }
        self.stop_words = set(get_stop_words('fr'))
        self.stop_words.update(common_words)
        self.original_question = question.lower()
        self.filtered_question = self.do_filter()
        self.parsed_question = self.do_parse()
        self.shortened_question = self.parsed_question

    def get_shortened_question(self):
        """
        getter final result
        """
        return self.shortened_question

    def do_filter(self):
        """
        suppress stop words (+ some) and ponctuation
        """
        question = (self.original_question).lower()
        question = re.sub("[']", ' ', question)
        listed_question = re.findall(r"[\w]+", question)
        listed_question.sort(key=lambda s: -len(s))
        self.filtered_question = " ".join(list(set(listed_question) -
                                               set(self.stop_words)))
        return self.filtered_question

    def do_parse(self):
        """
        analyze & parse to return a cleaned & filtered question
        """
        self.parsed_question = self.filtered_question
        return self.parsed_question

    def get_whole_question(self):
        """ just to avoid lint error """
        question = self.original_question
        return question
