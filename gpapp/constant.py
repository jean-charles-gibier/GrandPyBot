# -*- coding: utf-8 -*- #
"""
constantes yagp
"""

KEY_API_GG = 'AIzaSyDc8-o_WSdYwv8L3iFSWJVoYwj-7ls4dTM'

URL_API_GG_FMT = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
                 'input={}&key={}&inputtype=textquery&fields=formatted_address,geometry'

URL_API_WIKI_FMT = 'https://fr.wikipedia.org/w/api.php?' \
                 'action=opensearch&limit=1&namespace=0&format=json&search={}'
