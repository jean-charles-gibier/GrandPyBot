"""
Utilitaires *
 - traitement output
"""
import hashlib
import os
import random
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
        print("Get {} gg_answer".format(len(gg_answer["candidates"])))
        if len(gg_answer["candidates"]) > 0:
            self.formatted_address = gg_answer["candidates"][0]["formatted_address"]
            self.latitude = gg_answer["candidates"][0]["geometry"]["location"]["lat"]
            self.longitude = gg_answer["candidates"][0]["geometry"]["location"]["lng"]
        else:
            print("gg_answer status : '{}'".format(gg_answer["status"]))
        self.gg_maps_status = gg_answer["status"]

    def fetch_infos_from_wiki_media(self):
        """
        suppress stop words (+ some) and ponctuation
        """
        wiki_api = WikiMediaApi()
        print("Start wiki request")
        wiki_question = wiki_api.parse_address(self.formatted_address)
        print("Get {} wiki_question(s)".format(len(wiki_question)))
        if len(wiki_question) > 0:
            self.wiki_answer = wiki_api.opensearch(wiki_question)
            print("Get '{}' wiki_answer".format(self.wiki_answer))
            self.wiki_url = wiki_api.get_url()
            print("Get '{}' wiki_url".format(self.wiki_url))
            self.wiki_id = hashlib.md5(
                self.wiki_url.encode('utf-8')).hexdigest()
        elif self.gg_maps_status == "ZERO-RESULTS":
            print("Get wiki_question :''{}".format(wiki_question))
            self.wiki_answer = "Ok fiston, un peu spéciale ta demande là.<br>" \
                "Tu as gagné, je ne trouve rien à ce sujet  ..."
        else:
            print("Get wiki_question :''{}".format(wiki_question))
            self.wiki_answer = "Ok fiston, ta question semble ambigue.<br>" \
                               "J' ai un petit souci technique là ..."

    def get_barratin(self):
        """
        selectionne une entrée en matière au hasard
        """
        return random.choice([
            "Attends voir mon grand... l'adresse c'est :<br>",
            "Ah voilà ! Je t'explique où c'est :<br>",
            "Yep, je l'ai ! Or donc voici l'adresse :<br>",
            "C'est bon poussin, voilà ce que tu cherches :<br>",
            "Mmmh, si je ne me trompe pas c'est ici :<br>"
        ])

    def get_final_infos(self):
        """
        prepare display values
        """
        self.fetch_infos_from_google_map()
        self.fetch_infos_from_wiki_media()
        gg_key_api_map_load = os.getenv('GG_KEY_API_MAP_LOAD')
        print("GG_KEY_API_MAP_LOAD :'{}'".format(gg_key_api_map_load))
        if not self.wiki_answer.startswith("Ok fiston"):
            self.final_answer = \
                "{} {}<br><br>{}<br>{}<br><a href='{}'>[Lire la suite sur wikipedia]</a>" \
                .format(self.get_barratin(), self.formatted_address,
                        render_template('response_item.html',
                                        localisation=self.wiki_id,
                                        latitude=self.latitude,
                                        longitude=self.longitude,
                                        api_key=gg_key_api_map_load
                                        ),
                        self.wiki_answer, self.wiki_url)
        else:
            self.final_answer = self.wiki_answer
        return self.final_answer
