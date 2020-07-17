# -*- coding: utf-8 -*- #
"""
constantes yagp
"""

# KEY pour charger la map
KEY_API_MAP_LOAD_GG = 'AIzaSyAObn2Vc7C154ZfoVKPPMLKq6pustU_fbg'

# URL pour findplace (serveur)
URL_API_FIND_PLACE_GG = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
                 'input={}&key={}&inputtype=textquery&fields=formatted_address,geometry'

URL_API_WIKI_FMT = 'https://fr.wikipedia.org/w/api.php?' \
                 'action=opensearch&limit=1&namespace=0&format=json&search={}'
