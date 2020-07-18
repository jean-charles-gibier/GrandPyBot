"""
All the stuff for fetching info on wiki API
"""
import re
import time
import wikipediaapi


class WikiMediaApi:
    """
    main wiki class
    """

    def __init__(self):
        """
        Standard init
        """
        self.content = None
        self.ident = ""
        self.wiki_wiki = wikipediaapi.Wikipedia('fr')

    def get_id(self):
        """
        id unique de l'adresse selectionnee
        """
        return self.ident

    def opensearch(self, candidates):
        """
        test each candidates to fetch infos
        """
        try:
            for text in candidates:
                self.content = self.wiki_wiki.page(text)
                if self.content.exists():
                    return self.tokenize(self.content.text, 3)
        except Exception as err:
            print("Request error '{}', sleeping 5s".format(err))
            time.sleep(1)
        return candidates[0] if len(candidates) > 0 else \
            "Ok fiston tu m'as collé, je ne trouve rien !"

    def get_url(self):
        """
        return current url subject
        """
        return self.content.fullurl

    def tokenize(self, data, nb_sentences):
        """
        split data into chunk /sentences bounded by punctuation
        to take the firsts nb_sentences
        """
        sentences = re.split(r'\.[ \n]', data)[0:nb_sentences]
        return ". ".join(sentences) + "."

    def parse_address(self, to_parse):
        """
            # --[Dans text on a une adresse formattée GG]--
            # 7 Cité Paradis, 75010 Paris, France
            # ----------[ ou bien ]-----------------
            # 28 Rue Armand Carrel, 93100 Montreuil, France
            # ----------[ ou bien juste ]-----------------
            # 75001 Paris, France
            # ----[lancera une recherche sur]-----
            # Cité Paradis (Paris)
            # Rue Armand Carrel (Montreuil)
            #  ----[ puis  ]-----
            # Cité Paradis
            # Rue Armand Carrel
            #  ----[ puis (si pas de réponse) ]-----
            # Paris
            # Montreuil
        """
        address_to_check = []
        # Déjà on splite selon les virgules
        alter_address, address, zip_town, country = "", "", "", ""
        address_chunks = to_parse.split(',')
        # on compte
        nb_chunks = len(address_chunks)
        # si on a  plus de  3 chunks => autre adresse, adresse , CP Ville, PAYS
        if nb_chunks == 4:
            (alter_address, address, zip_town, country) = address_chunks
        # si on a 3 chunks => adresse , CP Ville, PAYS
        if nb_chunks == 3:
            (address, zip_town, country) = address_chunks
        elif nb_chunks == 2:
            (zip_town, country) = address_chunks
        elif nb_chunks == 1:
            (zip_town,) = address_chunks
            (country,) = address_chunks
        # on supprime les digits de la ville
        town = ''.join([i for i in zip_town if not i.isdigit()])
        #  on supprime les digits de l'address'
        address = ''.join([i for i in address if not i.isdigit()])
        if nb_chunks > 3:
            address_to_check.append("{} ({})".format(address.strip(), town.strip()))
            address_to_check.append("{} ({})".format(alter_address.strip(), town.strip()))
            address_to_check.append("{}".format(address.strip()))
            address_to_check.append("{}".format(alter_address.strip()))
        elif nb_chunks in (2, 3):
            address_to_check.append("{} ({})".format(address.strip(), town.strip()))
            address_to_check.append("{}".format(address.strip()))
        if town.strip() != "":
            address_to_check.append("{}".format(town.strip()))
        if country.strip() != "":
            address_to_check.append("{}".format(country.strip()))
        return address_to_check
