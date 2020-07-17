"""
Utilitaires *
 - traitement output
"""
import hashlib
import random
import gpapp.constant
from flask import render_template
from .google_api import GoogleApi
from .wiki_media_api import WikiMediaApi


class Answer:
    """
    Builds an answer from question
    """

    def __init__(self, question):
        """ init """
        self.short = question.get_shortened_question()
        self.latitude = 0
        self.longitude = 0
        self.formatted_address = ""
        self.wiki_url = ""
        self.wiki_id = ""
        self.wiki_answer = ""
        self.final_answer = ""
        self.gg_maps_status = ""

    def fetch_infos_from_google_map(self):
        """
        getter info from gg (gps coordinates 1rst)
        """
        gg_test = GoogleApi()
        gg_answer = gg_test.findplacefromtext(self.short)
        if len(gg_answer["candidates"]) > 0:
            self.formatted_address = gg_answer["candidates"][0]["formatted_address"]
            self.latitude = gg_answer["candidates"][0]["geometry"]["location"]["lat"]
            self.longitude = gg_answer["candidates"][0]["geometry"]["location"]["lng"]
        self.gg_maps_status = gg_answer["status"]

    def fetch_infos_from_wiki_media(self):
        """
        suppress stop words (+ some) and ponctuation
        """
        wiki_api = WikiMediaApi()
        wiki_question = wiki_api.parse_address(self.formatted_address)
        if len(wiki_question) > 0:
            self.wiki_answer = wiki_api.opensearch(wiki_question)
            self.wiki_url = wiki_api.get_url()
            self.wiki_id = hashlib.md5(self.wiki_url.encode('utf-8')).hexdigest()
        else:
            self.wiki_answer = "Ok fiston, tu m'accordes 5mn ?<br>" \
                               "J' ai un petit souci technique là ..."

    def get_barratin(self):
        """
        selectionne une entrée en matière au hasard
        """
        return random.choice([
            "Attends voir mon grand... Ah oui :",
            "Yep, c'est bon, je l'ai :",
            "Bien sûr mon poussin :",
            "Mmmh, si je ne me trompe pas :"
        ])

    def get_final_infos(self):
        """
        prepare display values
        """
        self.fetch_infos_from_google_map()
        self.fetch_infos_from_wiki_media()
        if not self.wiki_answer.startswith("Ok fiston"):
            self.final_answer = \
                "{} {}<br><br>{}<br>{}<br><a href='{}'>[Lire la suite sur wikipedia]</a>" \
                    .format(self.get_barratin(), self.formatted_address,
                            render_template('response_item.html',
                                            localisation=self.wiki_id,
                                            latitude=self.latitude,
                                            longitude=self.longitude,
                                            api_key=gpapp.constant.KEY_API_MAP_LOAD_GG
                                            ),
                            self.wiki_answer, self.wiki_url)
        else:
            self.final_answer = self.wiki_answer
        return self.final_answer
