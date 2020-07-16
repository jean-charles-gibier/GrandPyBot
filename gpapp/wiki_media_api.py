"""
All the stuff for fetching info on wiki API
"""

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
        self.wiki_wiki = wikipediaapi.Wikipedia('fr')

    """
    main wiki class
    gets links first
    """
    def opensearch(self, text):
        response = None
        try:
            # dans text on a une adresse formattée GG
            # 7 Cité Paradis, 75010 Paris, France
            # ou
            # 28 Rue Armand Carrel, 93100 Montreuil, France
            # lancera une recherche sur
            # Cité Paradis (Paris)
            # Rue Armand Carrel (Montreuil)
            # puis
            # Cité Paradis
            # Rue Armand Carrel
            # puis
            # Paris
            # Montreuil

            content = self.wiki_wiki.page(text)
            if content.exists():
                return content.text
            else:
                return text
        except Exception as e:
            print("Request error '{}', sleeping 5s".format(e.code))
            time.sleep(5)
        return []


